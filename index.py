import cv2     # computer vision library , image processing
import matplotlib.pyplot as plt   # image show 

image1 = cv2.imread('image1.jpg')    # BGR image read
image_rgb = cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)   # Convert BGR TO RGB
plt.imshow(image_rgb)  # show image 
plt.axis('off')  # remove axis
plt.show()  # show image

plt.title('Original Image')  # title of the image
plt.imshow(image_rgb)  # show image 
plt.show()  # show image
print('Image shape :', image_rgb.shape)  # print image shape

# Gray scale image
gray_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # Convert BGR TO GRAY
plt.title('Gray Scale Image')  # title of the image
plt.imshow(gray_image, cmap='gray') # 
plt.show()  # show image


# print at pixel value at (100,100)
pixel_value = gray_image[100, 100]  # get pixel value at (100,100)
print('Pixel value at (100,100):', pixel_value)  # print

resize = cv2.resize(image_rgb, (400,200)) # resize image to 200x200
plt.imshow(resize)  # show image 
plt.axis('off')  # remove axis
plt.show()  # show image

# Cropped Image
crop = image_rgb[100:600, 100:600]  # crop image from (100,100) to (400,400)
plt.imshow(crop)  # show image
plt.axis('off')  # remove axis
plt.show()  # show image