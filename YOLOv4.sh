#!/bin/bash

echo "### Bash Script: Explanation of Object Scanning AI Program ###"
echo
echo "1. **Import Required Libraries**:"
echo "   - The Python code uses 'cv2' for computer vision tasks, 'numpy' for numerical operations,"
echo "     and 'ultralytics' for the YOLOv8 object detection model."
echo
echo "2. **Load the YOLOv8 Pre-trained Model**:"
echo "   - The YOLOv8 model is loaded using the 'YOLO' class from the 'ultralytics' library."
echo "   - You can specify the model variant, such as 'yolov8n.pt' (nano), for balance between speed and accuracy."
echo
echo "3. **Capture Video Input:**"
echo "   - The program uses OpenCV to capture video frames."
echo "   - By default, it uses the webcam (source = 0), but you can provide a video file path."
echo
echo "4. **Object Detection and Drawing Bounding Boxes:**"
echo "   - For each frame:"
echo "       a) The YOLO model detects objects and returns bounding box coordinates, confidence scores, and class IDs."
echo "       b) Bounding boxes are drawn on the frame using OpenCV functions 'rectangle' and 'putText'."
echo
echo "5. **Displaying the Video Feed:**"
echo "   - The processed frame with object detections is displayed in a window titled 'Object Detection'."
echo "   - The user can quit the program by pressing the 'q' key."
echo
echo "6. **Releasing Resources:**"
echo "   - The video capture object is released, and all OpenCV windows are closed at the end."
echo
echo "### How to Run the Program: ###"
echo "   - Make sure Python and the required libraries ('opencv-python', 'numpy', 'ultralytics') are installed."
echo "   - Save the Python script to a file, e.g., 'object_detection.py'."
echo "   - Run the script with 'python object_detection.py'."
echo
echo "### Applications: ###"
echo "   - This program can be used for real-time object detection in various fields:"
echo "       * Autonomous vehicles"
echo "       * Security and surveillance"
echo "       * Inventory management"
echo "       * Robotics"
echo
echo "### Note: ###"
echo "   - You can customize the YOLO model, add additional preprocessing steps, or use video files as input."
echo
echo "Enjoy building your object scanning AI!"
