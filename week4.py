import cv2
import numpy as np

# Function to rotate an image by a given angle
def rotate_image(image, angle):
    # Get the dimensions of the image
    (height, width) = image.shape[:2]
    
    # Calculate the center of the image
    center = (width // 2, height // 2)
    
    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Perform the affine transformation (rotation)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    
    return rotated_image

# Load the image
image_path = r'C:\Users\ravik\OneDrive\Pictures\Saved Pictures\doremon.jpeg'
image = cv2.imread(image_path)

# Check if image is loaded successfully
if image is None:
    print(f"Error: Could not load image {image_path}")
else:
    # Rotate the image by various angles
    rotated_30 = rotate_image(image, 30)
    rotated_45 = rotate_image(image, 45)
    rotated_90 = rotate_image(image, 90)

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image (30 degrees)', rotated_30)
    cv2.imshow('Rotated Image (45 degrees)', rotated_45)
    cv2.imshow('Rotated Image (90 degrees)', rotated_90)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
