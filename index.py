import cv2  # computer vision library
import matplotlib.pyplot as plt  # image show

# Read the image
image1 = cv2.imread('image1.jpeg')

# Display the image
image_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

# Print its dimensions (shape)
print('3. Image dimensions (shape):', image_rgb.shape)

# Print the pixel value at (100,100)
# For color images, it returns [R, G, B]. For grayscale, a single intensity value.
gray_for_pixel = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
pixel_value = gray_for_pixel[100, 100]
print('4. Pixel value at (100,100):', pixel_value)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Print the grayscale image dimensions
print('6. Grayscale image dimensions:', gray_image.shape)

# Display the grayscale image
plt.title('Gray Scale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()

# Resize the image to 300 x 300
resize_img = cv2.resize(image_rgb, (300, 300))
plt.title('Resized Image (300x300)')
plt.imshow(resize_img)
plt.axis('off')
plt.show()

# Crop a portion of the image (e.g., from row 100 to 400, col 100 to 400)
crop_img = image_rgb[100:400, 100:400]
plt.title('Cropped Image')
plt.imshow(crop_img)
plt.axis('off')
plt.show()

# Save the grayscale image as gray_output.jpg
cv2.imwrite('gray_output.jpg', gray_image)
print('10. Grayscale image successfully saved as gray_output.jpg')