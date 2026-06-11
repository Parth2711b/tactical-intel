Football Analytics Pipeline – Progress Report

Step 1: Environment Setup ✅

Goal



Set up a Python environment capable of running computer vision and deep learning workloads efficiently.



Completed

Chose Google Colab as the development environment.

Enabled NVIDIA T4 GPU for accelerated inference.

Installed required dependencies:

ultralytics

supervision

opencv-python

yt-dlp

Outcome



Development environment successfully configured and ready for model inference.



Step 2: Video Acquisition \& Validation ✅

Goal



Download a football match video compatible with OpenCV and the analytics pipeline.



Challenges Encountered

Issue 1: Unsupported Video Format



The downloaded video was stored in .webm format using the AV1 codec, causing frame extraction issues with OpenCV.



Issue 2: Corrupted / Incomplete Video Reads



OpenCV opened the file but failed to read frames (ret=False), resulting in zero processed frames.



Resolution



Specified a compatible download format:



\-f "bestvideo\[height<=720]\[vcodec^=avc]+bestaudio\[ext=m4a]"

\--merge-output-format mp4



This ensured:



H.264 video codec

720p resolution

MP4 container

Full OpenCV compatibility

Validation Result

ret = True

frame shape = (720, 1280, 3)

Outcome



Successfully obtained a valid football match clip for processing.



Step 3: Player Detection \& Tracking Pipeline ✅

Goal



Detect players using YOLOv8 and track them across frames using ByteTrack.



Implementation

YOLOv8 used for player detection.

ByteTrack used for multi-object tracking.

Player positions exported to CSV for downstream analysis.

Challenges Encountered

Issue 1: Empty CSV Output



No detections were being recorded because frames were not being read correctly from the corrupted video.



Issue 2: Zero Frames Processed



The processing loop executed but no valid frames were available.



Issue 3: ByteTrack Deprecation Warning



Received a future deprecation warning from the Supervision library.



Resolution

Removed corrupted video files.

Forced fresh downloads.

Verified video integrity before processing.

Results

Metric	Value

Total Detections	57,064

Frames Processed	5,784

Unique Track IDs	1,081

Observation



The number of unique IDs is significantly higher than the actual number of players because ByteTrack frequently assigns new IDs when players leave and re-enter the camera view. This is expected when using a generic YOLO model and will improve with football-specific detection models.



Outcome



End-to-end player detection, tracking, and positional data extraction successfully completed.



Step 4: Automatic Team Color Assignment ✅

Goal



Automatically classify detected players into:



Team A

Team B

Others (referees, staff, etc.)

Methodology

Extract upper-body regions from player bounding boxes.

Compute representative jersey color features.

Apply K-Means clustering.

Assign clusters to teams based on cluster population size.

Challenges Encountered

Issue 1: Poor Frame Selection



Some sampled frames contained only a few visible players due to close-up camera shots.



Resolution



Scanned the video at regular intervals and selected the frame with the highest number of visible players.



Best frame selected: 24 visible players



Issue 2: Referee Misclassified as a Team Player



Initial clustering grouped referee colors with one of the teams.



Resolution



Used cluster population statistics:



Largest cluster → Team A

Second largest cluster → Team B

Smallest cluster → Others

Results

Category	Players

Team A	11

Team B	7

Others	6

Observation



A few players were incorrectly assigned to the "Others" category due to occlusions, small bounding boxes, and color ambiguity. Accuracy is expected to improve with football-specific models and additional appearance features.



Outcome



Automatic team classification successfully implemented.

