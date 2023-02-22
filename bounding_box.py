
from PIL import Image
from pytesseract import pytesseract
import cv2
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
image_path = r"C:/Users/vrdhn/Desktop/Inter IIT/interiit/interiit/fewer_imgs/Dataset_1591.jpeg"
  
# Opening the image & storing it in an image object
image=cv2.imread("C:/Users/vrdhn/Desktop/Untitled.png")
# img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
# text = pytesseract.image_to_string(img)
string=pytesseract.image_to_string(image)
  
# Displaying the extracted text
print(string[:-1])



# import cv2
# import numpy as np

# img = cv2.imread("C:/Users/vrdhn/Desktop/Inter IIT/interiit/interiit/images/Dataset_001.jpeg")

# # convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # threshold
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# # invert
# thresh = 255 - thresh

# # apply horizontal morphology close
# kernel = np.ones((5 ,191), np.uint8)
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# # get external contours
# contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours = contours[0] if len(contours) == 2 else contours[1]

# # draw contours
# result = img.copy()
# for cntr in contours:
#     # get bounding boxes
#     pad = 10
#     x,y,w,h = cv2.boundingRect(cntr)
#     print(x, y, w, h)
#     cv2.rectangle(result, (x-pad, y-pad), (x+w+pad, y+h+pad), (0, 0, 255), 4)

# # save result
# # cv2.imwrite("john_bbox.png",result)

# # display result
# cv2.imshow("thresh", thresh)
# cv2.imshow("morph", morph)
# cv2.imshow("result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()