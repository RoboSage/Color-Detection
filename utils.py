import numpy as np
import cv2

def get_limits(color):
    """
    This function takes a BGR color value and returns the lower and upper HSV 
    limits for color thresholding in OpenCV.

    Parameters:
    color (list): A list containing BGR values, e.g., [0, 255, 255] for yellow.

    Returns:
    tuple: (lowerLimit, upperLimit) - numpy arrays defining the lower and upper HSV bounds.
    """

    # Convert the BGR color to a NumPy array
    c = np.uint8([[color]])  # Creates a 1x1 pixel image with the given BGR color
    print(f"BGR color input: {color}")
    print(f"Converted to NumPy array: {c}")

    # Convert the single pixel BGR color to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # OpenCV function to convert BGR to HSV
    print(f"HSV representation: {hsvC}")

    # Extract the hue (H) value from the HSV representation
    hue = hsvC[0][0][0]  # Get the first (and only) pixel's hue value
    print(f"Extracted Hue value: {hue}")

    # Define saturation and value (brightness) thresholds
    min_saturation = 100
    min_value = 100
    max_saturation = 255
    max_value = 255

    # Handle the special case of red, which wraps around in the hue spectrum
    if hue >= 165:  # If the hue is in the upper red range (165-180)
        lowerLimit = np.array([hue - 10, min_saturation, min_value], dtype=np.uint8)
        upperLimit = np.array([180, max_saturation, max_value], dtype=np.uint8)
    elif hue <= 15:  # If the hue is in the lower red range (0-15)
        lowerLimit = np.array([0, min_saturation, min_value], dtype=np.uint8)
        upperLimit = np.array([hue + 10, max_saturation, max_value], dtype=np.uint8)
    else:
        # General case for other colors: define a range around the hue value
        lowerLimit = np.array([hue - 10, min_saturation, min_value], dtype=np.uint8)
        upperLimit = np.array([hue + 10, max_saturation, max_value], dtype=np.uint8)

    print(f"Lower HSV Limit: {lowerLimit}")
    print(f"Upper HSV Limit: {upperLimit}")

    return lowerLimit, upperLimit  # Return the HSV limits as numpy arrays


# Example usage
color = [0, 255, 255]  # Yellow in BGR
lower, upper = get_limits(color)
