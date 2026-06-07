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
