import cv2  # OpenCV library for computer vision tasks
from PIL import Image  # PIL (Pillow) for image processing in Python

from utils import get_limits  # Importing a custom function to get HSV limits for a given color

# Define common colors in BGR format (OpenCV uses BGR instead of RGB)
yellow = [0, 255, 255]   # Yellow in BGR
red = [0, 0, 255]        # Red in BGR
green = [0, 255, 0]      # Green in BGR
blue = [255, 0, 0]       # Blue in BGR
orange = [0, 165, 255]   # Orange in BGR
purple = [128, 0, 128]   # Purple in BGR
pink = [203, 192, 255]   # Pink in BGR
cyan = [255, 255, 0]     # Cyan in BGR
magenta = [255, 0, 255]  # Magenta in BGR
white = [255, 255, 255]  # White in BGR
black = [0, 0, 0]        # Black in BGR
gray = [128, 128, 128]   # Gray in BGR
brown = [19, 69, 139]    # Brown in BGR

# Initialize the webcam capture
cap = cv2.VideoCapture(0)  # 0 represents the default camera

while True:
    # Capture a single frame from the webcam
    ret, frame = cap.read()  # `ret` is a boolean (True if frame is captured successfully)
    
    # Convert the captured frame from BGR to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the lower and upper HSV limits for the yellow color
    lowerLimit, upperLimit = get_limits(color=yellow)

    # Create a binary mask where yellow pixels are highlighted (1) and everything else is black (0)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Convert the binary mask to a PIL Image for easier bounding box detection
    mask_ = Image.fromarray(mask)

    # Get the bounding box coordinates where yellow is detected
    bbox = mask_.getbbox()

    if bbox is not None:  # If yellow is detected in the frame
        x1, y1, x2, y2 = bbox  # Extract bounding box coordinates

        # Draw a green rectangle around the detected yellow region
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Display the mask output (showing only the detected yellow regions)
    cv2.imshow('frame', frame)

    # Exit condition: If 'q' key is pressed, break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
