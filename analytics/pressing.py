"""
analytics/pressing.py
----------------------
Quantify pressing intensity per team per time window.

Owner: P2 (analytics)
Depends on: positions_topview.csv

TODO:
- For each 15-min window:
    - Compute inter-player distance matrix between teams
    - Count frames where any defender is within threshold (e.g. 5m) of ball carrier
    - Normalize to pressing intensity score (0–100)
- Output: pressing_timeline.csv with columns [window, team_a_score, team_b_score]

Reference:
  Bekkers 2024 pressing intensity: https://arxiv.org/abs/2501.04712
"""
