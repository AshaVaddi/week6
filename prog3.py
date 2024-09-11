import cv2

# Function to crop a region from the image
def crop_image(image, x_start, y_start, x_end, y_end):
    # Cropping the image
    cropped_image = image[y_start:y_end, x_start:x_end]
    return cropped_image

# Load the image
image_path = r'C:\Users\ravik\OneDrive\Pictures\Saved Pictures\doremon.jpeg'
image = cv2.imread(image_path)

# Check if image is loaded successfully
if image is None:
    print(f"Error: Could not load image {image_path}")
else:
    # Define regions to crop (x_start, y_start, x_end, y_end)
    
    # Region 1: Top-left corner
    cropped_region_1 = crop_image(image, 0, 0, 200, 200)
    
    # Region 2: Center of the image
    height, width, _ = image.shape
    cropped_region_2 = crop_image(image, width // 4, height // 4, 3 * width // 4, 3 * height // 4)
    
    # Region 3: Bottom-right corner
    cropped_region_3 = crop_image(image, width - 200, height - 200, width, height)
    
    # Display the original image and cropped regions
    cv2.imshow('Original Image', image)
    cv2.imshow('Cropped Region 1 (Top-left)', cropped_region_1)
    cv2.imshow('Cropped Region 2 (Center)', cropped_region_2)
    cv2.imshow('Cropped Region 3 (Bottom-right)', cropped_region_3)
    
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
