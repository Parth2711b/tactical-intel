"""
analytics/formation.py
-----------------------
Detect formation (e.g. 4-3-3) from top-view player positions.

Owner: P2 (analytics)
Depends on: cv_pipeline/homography.py → positions_topview.csv

TODO:
- Load positions_topview.csv
- For each time window (e.g. every 5 min = N frames):
    - Filter players by team
    - Run KMeans to cluster positions into lines (defense, mid, attack)
    - Map cluster centroids to formation string using template matching
- Output: formation_timeline.csv with columns [minute, team_a_formation, team_b_formation]

Reference:
  EFPI paper: https://arxiv.org/abs/2506.23843
"""
