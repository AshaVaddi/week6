import cv2
import numpy as np

# Create a blank image (black background)
image = np.zeros((500, 500, 3), dtype='uint8')

# Draw a line
start_point = (50, 50)
end_point = (450, 50)
color = (255, 0, 0)  # Blue color in BGR
thickness = 5
cv2.line(image, start_point, end_point, color, thickness)

# Draw a rectangle
top_left_corner = (100, 100)
bottom_right_corner = (400, 300)
color = (0, 255, 0)  # Green color in BGR
thickness = 3
cv2.rectangle(image, top_left_corner, bottom_right_corner, color, thickness)

# Draw a filled rectangle
top_left_corner_filled = (150, 150)
bottom_right_corner_filled = (350, 250)
color_filled = (0, 0, 255)  # Red color in BGR
cv2.rectangle(image, top_left_corner_filled, bottom_right_corner_filled, color_filled, -1)

# Draw a circle
center = (250, 400)
radius = 50
color = (255, 255, 0)  # Cyan color in BGR
thickness = -1  # Filled circle
cv2.circle(image, center, radius, color, thickness)

# Draw an ellipse
center = (250, 200)
axes_length = (100, 50)
angle = 45  # Rotation angle
start_angle = 0
end_angle = 360
color = (0, 255, 255)  # Yellow color in BGR
thickness = 2
cv2.ellipse(image, center, axes_length, angle, start_angle, end_angle, color, thickness)

# Add text to the image
font = cv2.FONT_HERSHEY_SIMPLEX
text_position = (100, 450)
font_scale = 1
font_color = (255, 255, 255)  # White color in BGR
thickness = 2
cv2.putText(image, 'OpenCV Shapes', text_position, font, font_scale, font_color, thickness)

# Display the image with shapes
cv2.imshow('Shapes on Image', image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
