import cv2

# Load the image
image_path = r'C:\Users\ravik\OneDrive\Pictures\Saved Pictures\doremon.jpeg'
image = cv2.imread(image_path)

# Check if image is loaded successfully
if image is None:
    print(f"Error: Could not load image {image_path}")
else:
    # Convert BGR to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert BGR to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Convert BGR to LAB
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Display the original and converted images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.imshow('HSV Image', hsv_image)
    cv2.imshow('LAB Image', lab_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
