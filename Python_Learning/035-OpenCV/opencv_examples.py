import cv2
import numpy as np
import matplotlib.pyplot as plt

# This script will save image outputs to a 'temp_images' directory.
import os
if not os.path.exists('temp_images'):
    os.makedirs('temp_images')

# --- Image Generation (to have something to work with) ---
print("--- Generating a sample image ---")
# Create a simple 300x300 color image (as a NumPy array)
# It will have a black background by default
sample_image = np.zeros((300, 300, 3), dtype="uint8")
# Draw a white rectangle in the center
cv2.rectangle(sample_image, (50, 50), (250, 250), (255, 255, 255), -1) # -1 thickness for filled
# Draw a blue circle inside the rectangle
cv2.circle(sample_image, (150, 150), 75, (255, 0, 0), -1) # BGR color, so (255,0,0) is blue

# Save the generated image
generated_image_path = 'temp_images/generated_sample.png'
cv2.imwrite(generated_image_path, sample_image)
print(f"Sample image saved to: {generated_image_path}")


# --- Basic OpenCV Operations ---

# 1. Reading an Image
print("\n1. Reading an image with OpenCV")
# The '0' flag reads the image in grayscale
gray_image = cv2.imread(generated_image_path, 0)
# The '1' flag (or no flag) reads the image in color
color_image = cv2.imread(generated_image_path)

# Save the grayscale version
grayscale_path = 'temp_images/grayscale_sample.png'
cv2.imwrite(grayscale_path, gray_image)
print(f"   Grayscale version saved to: {grayscale_path}")
print(f"   Shape of color image: {color_image.shape}")
print(f"   Shape of grayscale image: {gray_image.shape}")


# 2. Color Space Conversion
print("\n2. Converting color spaces")
# As mentioned, OpenCV uses BGR by default. Matplotlib uses RGB.
# To display correctly with other libraries, we might need to convert.
image_rgb = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

# For demonstration, we'll use Matplotlib to show the difference
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(color_image)
axs[0].set_title('OpenCV BGR (Incorrect in Matplotlib)')
axs[1].imshow(image_rgb)
axs[1].set_title('Converted RGB (Correct in Matplotlib)')
color_conversion_path = 'temp_images/bgr_vs_rgb.png'
plt.savefig(color_conversion_path)
plt.close()
print(f"   BGR vs RGB comparison plot saved to: {color_conversion_path}")


# 3. Resizing an Image
print("\n3. Resizing an image")
# Let's resize our image to be 100x100 pixels
resized_image = cv2.resize(color_image, (100, 100), interpolation=cv2.INTER_AREA)
resized_path = 'temp_images/resized_sample.png'
cv2.imwrite(resized_path, resized_image)
print(f"   Resized image saved to: {resized_path}")
print(f"   Shape of resized image: {resized_image.shape}")


# 4. Applying a Gaussian Blur
print("\n4. Applying a Gaussian Blur filter")
# Blurring is often used to reduce image noise
# The kernel size (e.g., (7, 7)) must be odd numbers
blurred_image = cv2.GaussianBlur(color_image, (7, 7), 0)
blurred_path = 'temp_images/blurred_sample.png'
cv2.imwrite(blurred_path, blurred_image)
print(f"   Blurred image saved to: {blurred_path}")


# 5. Edge Detection
print("\n5. Detecting edges with Canny edge detector")
# Canny edge detection is a popular multi-stage algorithm
# It requires a grayscale image
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)
edges_path = 'temp_images/edges_sample.png'
cv2.imwrite(edges_path, edges)
print(f"   Edge-detected image saved to: {edges_path}")


# 6. Drawing on Images
print("\n6. Drawing shapes and text on an image")
# Let's draw on a copy of our original image
image_with_drawing = color_image.copy()

# Draw a green line
cv2.line(image_with_drawing, (0, 0), (300, 300), (0, 255, 0), 3) # Green line, 3px thick

# Put some text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_with_drawing, 'OpenCV Rocks!', (10, 290), font, 1, (0, 0, 255), 2, cv2.LINE_AA) # Red text

drawing_path = 'temp_images/drawing_sample.png'
cv2.imwrite(drawing_path, image_with_drawing)
print(f"   Image with drawings saved to: {drawing_path}")

print("\nAll OpenCV example images have been generated and saved.")
