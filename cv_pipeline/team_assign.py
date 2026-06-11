"""
cv_pipeline/team_assign.py
--------------------------
Assign detected players to Team A or Team B using K-means on jersey color.

Owner: P1 (cv-pipeline)
Depends on: detect.py (needs bounding boxes per frame)

TODO:
- Extract upper-half bounding box crop for each detection
- Convert crop to mean RGB
- Run KMeans(n_clusters=2) on RGB values across all players in first N frames
- Assign team label (0 or 1) to each tracker_id
- Add team column to positions CSV

Reference:
  https://github.com/Khushal-gupta22/Football-Analysis (team assignment section)
"""
