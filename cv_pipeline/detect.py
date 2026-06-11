"""
cv_pipeline/detect.py
---------------------
Step 1: Run YOLOv8 detection + ByteTrack on a video clip.
Outputs an annotated video and a CSV of per-frame player positions.

Owner: P1 (cv-pipeline)
"""

import cv2
import csv
import supervision as sv
from ultralytics import YOLO
from pathlib import Path


MODEL_PATH = "yolov8x.pt"  # swap with football-specific weights when ready
SOURCE_VIDEO = "data/samples/test_clip.mp4"
OUTPUT_VIDEO = "outputs/annotated.mp4"
OUTPUT_CSV   = "outputs/positions.csv"


def run(source: str = SOURCE_VIDEO, output_video: str = OUTPUT_VIDEO, output_csv: str = OUTPUT_CSV):
    Path("outputs").mkdir(exist_ok=True)

    model = YOLO(MODEL_PATH)
    tracker = sv.ByteTrack()
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    cap = cv2.VideoCapture(source)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w   = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h   = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["frame", "tracker_id", "x_center", "y_center", "confidence", "class"])

        frame_idx = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, verbose=False)[0]
            detections = sv.Detections.from_ultralytics(results)

            # Filter to persons only (class 0 in COCO)
            detections = detections[detections.class_id == 0]
            detections = tracker.update_with_detections(detections)

            # Write positions
            for i, tracker_id in enumerate(detections.tracker_id):
                x1, y1, x2, y2 = detections.xyxy[i]
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2
                writer.writerow([frame_idx, tracker_id, round(cx, 2), round(cy, 2),
                                  round(float(detections.confidence[i]), 3),
                                  detections.class_id[i]])

            # Annotate frame
            labels = [f"#{tid}" for tid in detections.tracker_id]
            frame = box_annotator.annotate(frame, detections)
            frame = label_annotator.annotate(frame, detections, labels)
            out.write(frame)
            frame_idx += 1

    cap.release()
    out.release()
    print(f"Done. Annotated video: {output_video}")
    print(f"Positions CSV: {output_csv}")


if __name__ == "__main__":
    run()
