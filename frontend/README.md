# Frontend

Owner: P4 (`feature/frontend`)

## Setup

```bash
npm create vite@latest . -- --template react
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install recharts axios
```

## What to build (in order)

1. **Video upload screen** — drag and drop, shows upload progress, polls `/status/{job_id}`
2. **Pitch minimap** — SVG overlay, team A dots (red) vs team B dots (blue), updates per frame scrub
3. **Formation timeline chart** — x-axis: match minute, y-axis: formation label per team
4. **Heatmap view** — toggle between team A / team B, time window selector
5. **Pressing intensity chart** — bar chart per 15-min window
6. **PDF export button** — calls jsPDF or triggers backend render

## API endpoints to connect to

| Action | Endpoint |
|---|---|
| Upload video | `POST /upload` |
| Poll progress | `GET /status/{job_id}` |
| Get results | `GET /results/{job_id}` |

## Notes

- Keep API base URL in a `.env` file: `VITE_API_URL=http://localhost:8000`
- All charts: use Recharts
- Pitch SVG: 105×68 aspect ratio, scale to fit container
