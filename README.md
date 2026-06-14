# ⚽ Tactical Intelligence Platform

AI-powered football match analysis — formation detection, heatmaps, and pressing metrics from uploaded video. No expensive subscriptions needed.

---

## What this does

Upload a football match clip → get back:
- **Formation timeline** — how both teams' shape changed across the match
- **Heatmaps** — per-team and per-player positional density
- **Pressing intensity** — quantified per 15-minute window
- **Shareable report** — one-click PDF export

---

## Tech Stack

| Layer | Tools |
|---|---|
| Detection | YOLOv8x |
| Tracking | ByteTrack (via Supervision) |
| Team ID | K-means on jersey color |
| Pitch mapping | Homography (OpenCV) |
| Heatmaps | Supervision HeatMapAnnotator |
| Formation | EFPI method (arXiv:2506.23843) |
| Backend | FastAPI |
| Frontend | React + Tailwind |

---

## Repo Structure

```
tactical-intel/
├── cv_pipeline/        # Detection, tracking, homography, team assignment
├── analytics/          # Formation detection, heatmaps, pressing metrics
├── backend/            # FastAPI server, video processing pipeline
├── frontend/           # React dashboard
├── data/
│   └── samples/        # Test clips (not committed, add to .gitignore)
└── docs/               # Architecture notes, research references
```

---

## Branch Strategy

| Branch | Purpose |
|---|---|
| `main` | Stable, demo-ready only. No direct pushes. |
| `dev` | Integration branch. All features merge here first. |
| `feature/cv-pipeline` | Player detection, tracking, pitch mapping |
| `feature/analytics` | Formation, heatmaps, pressing |
| `feature/backend` | FastAPI server + pipeline |
| `feature/frontend` | React dashboard + export |

**Workflow:**
1. Work on your feature branch
2. Open a PR → `dev`
3. One other person reviews
4. Merge to `main` only when a full feature is working end-to-end

---

## Setup

```bash
git clone https://github.com/Parth2711b/tactical-intel.git
cd tactical-intel
pip install -r requirements.txt
```

> **No GPU locally?** Use Google Colab with T4 GPU (free). See `docs/colab_setup.md`.

---

## Run the backend locally

Quick commands to run the FastAPI backend from the project root:

```powershell
# start in background (PowerShell)
Start-Process -NoNewWindow -FilePath python -ArgumentList '-m','uvicorn','main:app','--app-dir','backend','--host','127.0.0.1','--port','8000' -WorkingDirectory "$PWD"

# or run foreground (shows logs)
python -m uvicorn main:app --app-dir backend --host 127.0.0.1 --port 8000
```

API docs (Swagger UI): http://127.0.0.1:8000/docs

Quick end-to-end local test (creates a dummy MP4 and exercises upload → process → results):

```bash
python backend_test.py
```

The backend currently implements a placeholder background pipeline (see `backend/main.py`) that simulates formation, heatmap generation, and pressing metrics. Replace with real CV/analytics modules when ready.

## Local utility scripts (optional)

There are a few convenience scripts under the local `scripts/` folder that are kept untracked on this machine. They are helpful for development and testing but are intentionally not pushed to the repository by default.

- `scripts/generate_heatmaps.py` — synthesize example heatmaps (uses NumPy + OpenCV).
- `scripts/cleanup_results.py` — remove low-variance (solid-color) placeholder images from `data/results/`.
- `scripts/inspect_results.py` — print simple stats (std/min/max) for images in `data/results/`.

Notes:
- These scripts require the following Python packages if you want to run them locally: `numpy`, `opencv-python`, and `Pillow` (install with `pip install numpy opencv-python Pillow`).
- The `data/results/` directory is ignored by Git for generated images, but the repository keeps a `.gitkeep` so the folder exists.
- Keeping the scripts local avoids committing machine-specific utilities or temporary helpers. If you want these shared, consider committing them to a feature branch (for example `dev/utils`).

---

## Team

| Person | Branch | Owns |
|---|---|---|
| P1 | `feature/cv-pipeline` | Detection, tracking, homography |
| P2 | `feature/analytics` | Formation, heatmaps, pressing |
| P3 | `feature/backend` | FastAPI, video pipeline |
| P4 | `feature/frontend` | React dashboard, PDF export |

---

## References

- [roboflow/sports](https://github.com/roboflow/sports) — base pipeline
- [SoccerNet](https://www.soccer-net.org/) — training data
- [EFPI paper](https://arxiv.org/abs/2506.23843) — formation detection method
- [Pressing intensity metric](https://arxiv.org/abs/2501.04712) — Bekkers 2024
