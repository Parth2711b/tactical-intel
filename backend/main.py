"""
backend/main.py
---------------
FastAPI server — video upload + analysis endpoints.

Owner: P3 (backend)

Run with:
  uvicorn backend.main:app --reload
"""

from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uuid, shutil
from pathlib import Path
import cv2
import numpy as np

app = FastAPI(title="Tactical Intelligence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("data/uploads")
RESULT_DIR = Path("data/results")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
RESULT_DIR.mkdir(parents=True, exist_ok=True)

# In-memory job status store (replace with Redis/DB later)
jobs: dict = {}


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}


@app.post("/api/v1/videos")
async def upload_video(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".mp4"):
        raise HTTPException(status_code=400, detail="Only MP4 video uploads are supported")

    job_id = str(uuid.uuid4())
    save_path = UPLOAD_DIR / f"{job_id}_{Path(file.filename).name}"

    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    jobs[job_id] = {"status": "queued", "file": str(save_path)}
    background_tasks.add_task(run_pipeline, job_id, str(save_path))

    return {"job_id": job_id, "status": "queued"}


@app.get("/api/v1/jobs/{job_id}")
def get_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="job_id not found")
    return jobs[job_id]


@app.get("/api/v1/jobs/{job_id}/results")
def get_results(job_id: str):
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="job_id not found")

    if job["status"] == "failed":
        raise HTTPException(status_code=500, detail={"status": "failed", "error": job.get("error")})

    if job["status"] != "done":
        raise HTTPException(status_code=202, detail={"status": job["status"], "message": "results are not ready yet"})

    return job.get("results", {})


def create_placeholder_heatmap(path: Path, color: tuple):
    image = np.zeros((360, 640, 3), dtype=np.uint8)
    cv2.rectangle(image, (0, 0), (639, 359), color, thickness=-1)
    cv2.putText(
        image,
        path.name,
        (20, 180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    cv2.imwrite(str(path), image)


def run_pipeline(job_id: str, video_path: str):
    """Background task — plug in cv_pipeline and analytics modules here."""
    jobs[job_id]["status"] = "processing"
    try:
        # TODO: replace this simulated pipeline with real CV + analytics logic
        formation_timeline = [
            {"minute": 0, "team_a_formation": "4-3-3", "team_b_formation": "4-2-3-1"},
            {"minute": 15, "team_a_formation": "4-3-3", "team_b_formation": "5-3-2"},
            {"minute": 30, "team_a_formation": "4-2-3-1", "team_b_formation": "4-4-2"},
            {"minute": 45, "team_a_formation": "3-4-3", "team_b_formation": "4-4-2"},
        ]

        heatmap_a = RESULT_DIR / f"{job_id}_heatmap_team_a.png"
        heatmap_b = RESULT_DIR / f"{job_id}_heatmap_team_b.png"
        create_placeholder_heatmap(heatmap_a, (64, 128, 255))
        create_placeholder_heatmap(heatmap_b, (255, 128, 64))

        pressing_timeline = [
            {"window": "0-15", "team_a_score": 68, "team_b_score": 55},
            {"window": "15-30", "team_a_score": 74, "team_b_score": 61},
            {"window": "30-45", "team_a_score": 71, "team_b_score": 58},
        ]

        jobs[job_id]["results"] = {
            "formation_timeline": formation_timeline,
            "heatmap_paths": {
                "team_a": str(heatmap_a),
                "team_b": str(heatmap_b),
            },
            "pressing_timeline": pressing_timeline,
        }
        jobs[job_id]["status"] = "done"
    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)
