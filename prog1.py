import cv2

# Function to load and display an image
def display_image(file_path):
    # Read the image from the file
    image = cv2.imread(file_path)
    
    # Check if image is loaded successfully
    if image is None:
        print(f"Error: Could not load image {file_path}")
        return
    
    # Display the image in a window
    cv2.imshow('Image', image)
    
    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test with different image formats (PNG, JPEG)
image_paths = [
    r"C:\Users\ravik\OneDrive\Pictures\Saved Pictures\doremon.jpeg", 
    r"C:\Users\ravik\OneDrive\Pictures\Saved Pictures\wp4012190.jpg"
]

# Loop through the image paths and display each one
for path in image_paths:
    display_image(path)
