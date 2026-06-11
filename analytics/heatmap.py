"""
analytics/heatmap.py
---------------------
Generate heatmaps from top-view player positions.

Owner: P2 (analytics)
Depends on: positions_topview.csv

TODO:
- Load positions_topview.csv
- Filter by team (team=0 or team=1)
- Optional: filter by time window
- Use sv.HeatMapAnnotator or matplotlib KDE to render heatmap on pitch template
- Output: heatmap_team_a.png, heatmap_team_b.png (and time-windowed versions)
"""
