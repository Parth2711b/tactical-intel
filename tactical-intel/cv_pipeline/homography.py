"""
cv_pipeline/homography.py
--------------------------
Map pixel coordinates → real-world pitch coordinates (105 x 68 m).

Owner: P1 (cv-pipeline)
Depends on: detect.py positions CSV

TODO:
- Load YOLOv8-pose pitch keypoint model (32 keypoints)
- For each frame, detect visible keypoints
- Compute homography matrix: cv2.findHomography(src_pts, dst_pts)
  where dst_pts are known real-world positions on a 105x68 pitch
- Transform each player (cx, cy) → (real_x, real_y)
- Output: positions_topview.csv with columns [frame, tracker_id, real_x, real_y, team]

Reference:
  https://blog.roboflow.com/camera-calibration-sports-computer-vision/
  Pitch keypoint model: roboflow/sports repo (soccer example)
"""
