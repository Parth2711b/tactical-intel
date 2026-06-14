# Task Board

> Update this file when you pick up or complete a task. Keep it honest.
> Status: 🔲 Not started | 🔄 In progress | ✅ Done | 🚧 Blocked

---

## Phase 1 — Foundation (Week 1–2)
Goal: minimap working on a test clip end-to-end.

| Task | Owner | Branch | Status | Notes |
|---|---|---|---|---|
| Clone roboflow/sports, run existing pipeline on test clip | P1 | `feature/cv-pipeline` | 🔲 | Use any YouTube match clip |
| YOLOv8x player + ball + referee detection | P1 | `feature/cv-pipeline` | 🔲 | Use Roboflow pretrained model |
| ByteTrack integration — persistent player IDs | P1 | `feature/cv-pipeline` | 🔲 | Via supervision library |
| K-means team color assignment | P1 | `feature/cv-pipeline` | 🔲 | K=2, upper bounding box RGB |
| Pitch keypoint detection (32 keypoints) | P1 | `feature/cv-pipeline` | 🔲 | YOLOv8-pose on pitch |
| Homography — pixel to real-world coords | P1 | `feature/cv-pipeline` | 🔲 | cv2.findHomography |
| Export per-frame positions to CSV | P1 | `feature/cv-pipeline` | 🔲 | Input for all analytics modules |
| FastAPI project scaffold | P3 | `feature/backend` | ✅ | Implemented in `backend/main.py` (versioned endpoints, MP4 validation) |
| React project scaffold | P4 | `feature/frontend` | 🔲 | Vite + Tailwind setup |

---

## Phase 2 — Intelligence Layer (Week 3–4)
Goal: formation detection + heatmap working on uploaded clip.

| Task | Owner | Branch | Status | Notes |
|---|---|---|---|---|
| Heatmap generation from position CSV | P2 | `feature/analytics` | 🔲 | sv.HeatMapAnnotator, per-team toggle |
| Formation clustering (K-means on top-view coords) | P2 | `feature/analytics` | 🔲 | Read EFPI paper first |
| Formation string mapping (4-3-3, 4-4-2 etc.) | P2 | `feature/analytics` | 🔲 | Template matching |
| Formation timeline — per 5-min window | P2 | `feature/analytics` | 🔲 | Output: list of (timestamp, formation) |
| Pressing intensity per 15-min window | P2 | `feature/analytics` | 🔲 | Inter-player distance matrix |
| Video upload endpoint (FastAPI) | P3 | `feature/backend` | 🔲 | Multipart upload |
| Async processing + progress polling | P3 | `feature/backend` | ✅ | BackgroundTasks implemented; tested via `backend_test.py` |
| Pitch minimap component (React) | P4 | `feature/frontend` | 🔲 | SVG overlay, player dots |
| Formation timeline chart | P4 | `feature/frontend` | 🔲 | Chart.js or Recharts |

---

## Phase 3 — Platform (Week 5–6)
Goal: full platform demo, shareable report.

| Task | Owner | Branch | Status | Notes |
|---|---|---|---|---|
| Connect frontend to backend API | P3 + P4 | both | 🔲 | CORS, response schema |
| Heatmap toggle UI (per team, time window) | P4 | `feature/frontend` | 🔲 | |
| PDF report export | P4 | `feature/frontend` | 🔲 | jsPDF or backend-rendered |
| Opponent scouting mode (multi-clip upload) | P2 + P3 | both | 🔲 | v2 stretch goal |
| End-to-end demo on real match clip | All | `dev` | 🔲 | Merge everything to dev |

---

## Blockers / Notes

- Add blockers here as you find them
- If stuck for >1 day, flag in group chat with what you tried
