import cv2
import numpy as np

# Function to resize an image with different interpolation methods
def resize_image(image, scale_percent, interpolation):
    # Calculate the new dimensions
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dimensions = (width, height)
    
    # Resize the image
    resized = cv2.resize(image, dimensions, interpolation=interpolation)
    return resized

# Load the image
image_path = r'C:\Users\ravik\OneDrive\Pictures\Saved Pictures\doremon.jpeg'
image = cv2.imread(image_path)

# Check if image is loaded successfully
if image is None:
    print(f"Error: Could not load image {image_path}")
else:
    # Resize the image using different interpolation methods
    scale_percent = 50  # Resizing to 50% of original size

    resized_nearest = resize_image(image, scale_percent, cv2.INTER_NEAREST)
    resized_linear = resize_image(image, scale_percent, cv2.INTER_LINEAR)
    resized_cubic = resize_image(image, scale_percent, cv2.INTER_CUBIC)

    # Display the original and resized images
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image (INTER_NEAREST)', resized_nearest)
    cv2.imshow('Resized Image (INTER_LINEAR)', resized_linear)
    cv2.imshow('Resized Image (INTER_CUBIC)', resized_cubic)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
