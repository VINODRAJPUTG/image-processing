import cv2

# =============================================================================
# cap = cv2.VideoCapture("C:\\Users\\Admin\\OneDrive\\Desktop\\bh.mp4")
# print("cap",cap)
# while True:
#     ret,frame = cap.read()
#     frame = cv2.resize(frame,(700,450))
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame",gray)
#     # cv2.imshow("frame",frame)
#     k = cv2.waitKey(25)
#     if k == ord("q") &0xFF:
#         break
# =============================================================================


# capture video by web camera


cap = cv2.VideoCapture(0)
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")

#it contains four parameters , name,codec, fps, resolution
output = cv2.VideoWriter("D:\\output.avi",fourcc,20.0,(640,480))
print(cap)

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        # frame = cv2.resize(frame,(500,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,0)
        cv2.imshow("gray",gray)
        cv2.imshow("frame",frame)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"): # to exit
            break  


  
cap.release()
output.release()
cv2.destroyAllWindows()
