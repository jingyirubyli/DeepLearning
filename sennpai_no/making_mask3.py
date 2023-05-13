import cv2
import numpy as np
import glob
import os

save_path="./mask_ivc_liver_ishikawa/"

if os.path.exists(save_path)==False:
    os.mkdir(save_path) 

files = glob.glob("./result_ivc_liver/*.png")

for file in files:
    img_origin = cv2.imread(file, 1)
    
    basename=os.path.basename(file) 


#この下増やす
    bgrLower = np.array([0, 0, 120])    # 抽出する色の下限(BGR)
    bgrUpper = np.array([100, 100, 255])    # 抽出する色の上限(BGR)
    img_cont = cv2.inRange(img_origin, bgrLower, bgrUpper) # BGRからマスクを作成

    bgrLower_2 = np.array([120, 0, 0])    # 抽出する色の下限(BGR)
    bgrUpper_2 = np.array([255, 160, 100])    # 抽出する色の上限(BGR)
    img_cont_2 = cv2.inRange(img_origin, bgrLower_2, bgrUpper_2) # BGRからマスクを作成

    h, w, _ = img_origin.shape
    blank = np.zeros((h, w, 1))

    ret, img_binary = cv2.threshold(img_cont, 150, 255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    ret_2, img_binary_2 = cv2.threshold(img_cont_2, 150, 255,cv2.THRESH_BINARY)
    contours_2, hierarchy_2 = cv2.findContours(img_binary_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    img_contour = cv2.drawContours(blank, contours, -1, (1, 1, 1), -1)
    img_contour = cv2.drawContours(img_contour, contours_2, -1, (2 , 2, 2), -1)

    cv2.imwrite(save_path +basename , img_contour)



# cv2.imshow("",img_contour)
# cv2.waitKey(0)
# cv2.destroyAllWindows()