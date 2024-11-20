# import image in 3 channel(colourful)
import cv2 
# =============================================================================
# img1 = cv2.imread("D:\\prem.jpeg",1)
# print(img1)
# cv2.imshow("3 channel ",img1)
# 
# 
# 
# 
# # import image in 1 channel(gray scale)
# 
# img2 = cv2.imread("D:\\prem.jpeg",0)
# print(img2)
# cv2.imshow("gray scale ",img2)
# 
# 
# 
# # unchanged image to improve color saturation
# img2 = cv2.imread("D:\\prem.jpeg",-1)
# print(img2)
# cv2.imshow("Unchanged image ",img2)
# 
# 
# 
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================



# write a program to take a image as a user input and
# change it into gray scale and save it 

path = input("Enter your image location   ")
print("you image location is  :   ",path)
img3 = cv2.imread(path,0)
img3 = cv2.resize(img3,(700,700))
img3 = cv2.flip(img3,1)# it accept 0,1,-1
cv2.imshow("converted image is  : ",img3)

# to save
k = cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("D:\\output.png",img3)
else:
    cv2.destroyAllWindows()


