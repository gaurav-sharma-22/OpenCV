import cv2
#reading image
image = cv2.imread("img\goku.jpg") 
#converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image inversion  to enhance details
inverted_image = 255-gray_image
#creating pencil sketch
blurred = cv2.GaussianBlur(inverted_image,(35,35),0)
inverted_blurred = 255-blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred , scale=105.0)
#displaying image using OpenCV
cv2.imshow("original Image", image)
cv2.imshow("pencil sketch of Image", pencil_sketch)
cv2.waitKey(0)