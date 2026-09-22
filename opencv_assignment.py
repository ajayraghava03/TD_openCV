import cv2
import numpy as np



image = cv2.imread("input.jpg")

if image is None:
    print("Error: Could not read the image.")
    exit()

cv2.imshow("Original Image", image)
cv2.imwrite("saved_image.jpg", image)



resized = cv2.resize(image, (500, 400))
cv2.imshow("Resized Image", resized)




horizontal_flip = cv2.flip(image, 1)
cv2.imshow("Horizontal Flip", horizontal_flip)


vertical_flip = cv2.flip(image, 0)
cv2.imshow("Vertical Flip", vertical_flip)


both_flip = cv2.flip(image, -1)
cv2.imshow("Both Flips", both_flip)




drawing = image.copy()


cv2.line(drawing, (50, 50), (300, 50), (0, 255, 0), 3)


points = np.array([
    [100, 100],
    [200, 80],
    [300, 150],
    [200, 220]
], np.int32)

cv2.polylines(drawing, [points], True, (255, 0, 0), 3)


cv2.putText(
    drawing,
    "OpenCV",
    (100, 300),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

cv2.imshow("Drawing and Text", drawing)




rows, cols = image.shape[:2]


translation_matrix = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

translated = cv2.warpAffine(
    image,
    translation_matrix,
    (cols, rows)
)

cv2.imshow("Translated Image", translated)



center = (cols // 2, rows // 2)

rotation_matrix = cv2.getRotationMatrix2D(
    center,
    45,
    1.0
)

rotated = cv2.warpAffine(
    image,
    rotation_matrix,
    (cols, rows)
)

cv2.imshow("Rotated Image", rotated)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresholded = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Binary Threshold", thresholded)



gaussian_blur = cv2.GaussianBlur(
    image,
    (7, 7),
    0
)

cv2.imshow("Gaussian Blur", gaussian_blur)



median_blur = cv2.medianBlur(
    image,
    7
)

cv2.imshow("Median Blur", median_blur)




kernel = np.ones((5, 5), np.uint8)


tophat = cv2.morphologyEx(
    image,
    cv2.MORPH_TOPHAT,
    kernel
)

cv2.imshow("TopHat", tophat)


blackhat = cv2.morphologyEx(
    image,
    cv2.MORPH_BLACKHAT,
    kernel
)

cv2.imshow("BlackHat", blackhat)




edges = cv2.Canny(
    gray,
    100,
    200
)

cv2.imshow("Canny Edge Detection", edges)




cv2.imwrite("resized.jpg", resized)
cv2.imwrite("horizontal_flip.jpg", horizontal_flip)
cv2.imwrite("vertical_flip.jpg", vertical_flip)
cv2.imwrite("translated.jpg", translated)
cv2.imwrite("rotated.jpg", rotated)
cv2.imwrite("threshold.jpg", thresholded)
cv2.imwrite("gaussian_blur.jpg", gaussian_blur)
cv2.imwrite("median_blur.jpg", median_blur)
cv2.imwrite("edges.jpg", edges)



cv2.waitKey(0)
cv2.destroyAllWindows()




cap = cv2.VideoCapture("input_video.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")
else:

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        "output_video.mp4",
        fourcc,
        fps,
        (width, height)
    )

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        
        gray_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        
        processed_frame = cv2.cvtColor(
            gray_frame,
            cv2.COLOR_GRAY2BGR
        )

        cv2.imshow(
            "Original Video",
            frame
        )

        cv2.imshow(
            "Processed Video",
            processed_frame
        )

        out.write(processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()




webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Error: Could not open webcam.")
else:

    while True:

        ret, frame = webcam.read()

        if not ret:
            print("Could not read frame.")
            break

        
        gray_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        cv2.imshow(
            "Live Webcam",
            frame
        )

        cv2.imshow(
            "Live Grayscale",
            gray_frame
        )

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()