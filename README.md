# OpenCV Computer Vision Practicals
A comprehensive OpenCV and Python assignment project demonstrating core Computer Vision operations including image processing, geometric transformations, filtering, edge detection, video file processing, and live webcam feed manipulation.
---
## 📌 Project Overview
This repository contains `opencv_assignment.py`, a complete practical demonstration of essential Computer Vision techniques using standard Python libraries: `opencv-python` and `numpy`. 
The project performs operations across three main media types:
1. **Static Image Processing** (`input.jpg`)
2. **Video File Processing** (`input_video.mp4`)
3. **Real-time Webcam Streaming** (Camera Index `0`)
---
##  Features & Covered Concepts
### 1. Image I/O & Manipulation
- **Read & Display**: Reads `input.jpg` and presents window previews.
- **Exporting Images**: Saves modified output frames to disk.
- **Resizing**: Rescales image dimensions to `(500, 400)` pixels.
- **Flipping**:
  - Horizontal Flip (`cv2.flip(image, 1)`)
  - Vertical Flip (`cv2.flip(image, 0)`)
  - Both Axes Flip (`cv2.flip(image, -1)`)
### 2. Drawing Primitives & Text Annotation
- **Line Drawing**: Renders custom colored lines (`cv2.line`).
- **Polygon Drawing**: Draws filled/unfilled multi-vertex polylines (`cv2.polylines`).
- **Text Rendering**: Overlays custom text onto images (`cv2.putText`).
### 3. Geometric Transformations
- **Translation**: Shifts image along X and Y axes using affine warp matrices (`cv2.warpAffine`).
- **Rotation**: Rotates image by $45^\circ$ around its center point (`cv2.getRotationMatrix2D`).
### 4. Image Thresholding & Grayscale Conversion
- **Grayscale Conversion**: Converts BGR color space to Grayscale (`cv2.COLOR_BGR2GRAY`).
- **Binary Thresholding**: Applies fixed thresholding ($127$ cut-off value) (`cv2.threshold`).
### 5. Image Blurring & Filtering
- **Gaussian Blur**: Smooths images using Gaussian kernel matrix ($7\times7$) (`cv2.GaussianBlur`).
- **Median Blur**: Reduces noise using median filtering ($7$ kernel size) (`cv2.medianBlur`).
### 6. Morphological Operations
- **Top Hat Filter**: Highlights bright elements smaller than the structuring element ($5\times5$) (`cv2.MORPH_TOPHAT`).
- **Black Hat Filter**: Highlights dark elements smaller than the structuring element ($5\times5$) (`cv2.MORPH_BLACKHAT`).
### 7. Edge Detection
- **Canny Edge Detection**: Detects sharp structural boundaries and contours (`cv2.Canny`).
### 8. Video Stream Processing
