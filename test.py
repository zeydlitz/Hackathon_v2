
import cv2
import numpy as np
import copy
# # read image
src = cv2.imread(r'Testers\tester_1\j.png')
# img = np.zeros((len(src),len(src[0])), np.uint8)
# cv2.imshow("Gaussian Smoothing", img)
# cv2.imshow("Gaussian Smoothing", )
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # apply guassian blur on src image
# dst = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
#
# # display input and output image
#cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
# cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image
# img = np.zeros((,), np.uint8)
# cv2.imshow("Gaussian Smoothing", img)
# cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image
# color = np.uint8(np.random.rand(3) * 255).tolist()
# print(color)
h=[[160 ,115], [371 ,95], [628, 47], [661, 545], [760, 550], [760 ,700], [165 ,680], [145 ,550], [175 ,542], [160, 115]]

mask = np.zeros(src.shape, np.uint8)
test=copy.deepcopy(src)
cv2.fillPoly(mask,np.array([h], dtype=np.int32), (255,255,255))
cv2.rectangle(test,(0,0),(src.shape[1],src.shape[0]), (0,255,0),-1)
cv2.copyTo(src,mask,test)
RGB1,RGB2=[56, 86, 97], [126, 156, 167]
check = test[0, 0]
counterW, counterB = 0, 0
OutputImage = cv2.inRange(test, tuple(RGB1), tuple(RGB2))
for i in range(test.shape[0]):
    for j in range(test.shape[1]):
        if list(test[i, j]) == list(check):
            if OutputImage[i, j] == 255:
                counterW += 1
            else:
                counterB += 1
                OutputImage[i][j] = 120
cv2.imwrite(r'Testers\tut\tut_v\OutputImage.jpg', OutputImage)
# mask1 = np.ones(src.shape,np.uint8)
# mask1.fill(255)
# cv2.fillPoly(mask1, np.array([h], dtype=np.int32), (0, 216, 255))
# mask2 = np.ones(src.shape,np.uint8)
# mask2.fill(255)
# cv2.bitwise_and(src,mask1,mask2)
# test = copy.deepcopy(src)
# mask = np.zeros(src.shape, np.uint8)
# cv2.fillPoly(mask, np.array([h], dtype=np.int32), (255, 255, 255))
# cv2.rectangle(src, (0, 0), (src.shape[1],src.shape[0]), (0, 255, 0), -1)
# cv2.copyTo(test, mask, src)
cv2.imshow("Nice", test)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image