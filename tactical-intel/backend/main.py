"""
backend/main.py
---------------
FastAPI server — video upload + analysis endpoints.

Owner: P3 (backend)

Run with:
  uvicorn backend.main:app --reload
"""

from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import uuid, shutil
from pathlib import Path

app = FastAPI(title="Tactical Intelligence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# In-memory job status store (replace with Redis/DB later)
jobs: dict = {}


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/upload")
async def upload_video(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    save_path = UPLOAD_DIR / f"{job_id}_{file.filename}"

    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    jobs[job_id] = {"status": "queued", "file": str(save_path)}
    background_tasks.add_task(run_pipeline, job_id, str(save_path))

    return {"job_id": job_id, "status": "queued"}


@app.get("/status/{job_id}")
def get_status(job_id: str):
    if job_id not in jobs:
        return {"error": "job not found"}
    return jobs[job_id]


@app.get("/results/{job_id}")
def get_results(job_id: str):
    # TODO: return formation_timeline, heatmap paths, pressing_timeline
    job = jobs.get(job_id)
    if not job or job["status"] != "done":
        return {"error": "results not ready"}
    return job.get("results", {})


def run_pipeline(job_id: str, video_path: str):
    """Background task — plug in cv_pipeline and analytics modules here."""
    jobs[job_id]["status"] = "processing"
    try:
        # TODO: call cv_pipeline.detect.run(video_path)
        # TODO: call cv_pipeline.team_assign
        # TODO: call cv_pipeline.homography
        # TODO: call analytics.formation
        # TODO: call analytics.heatmap
        # TODO: call analytics.pressing
        jobs[job_id]["status"] = "done"
        jobs[job_id]["results"] = {}  # fill with actual output paths
    except Exception as e:
        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)
