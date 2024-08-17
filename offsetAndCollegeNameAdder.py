import cv2
import PIL
from PIL import Image   

folder = 'banner'

final = cv2.imread('banner/offset.png')

(w,h,d) = final.shape

hplace = 30
hplace = int(hplace)
wplace = w*0.3
wplace = int(wplace)
# print("width={},height={}".format(w,h))
name = 'BHARTI VIDYAPEETH COLLEGE OF ENGINEERING PLACEMENT'

cv2.putText(final,name,(wplace,hplace),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
# cv2.line(final,(0,40),(w,40),(0,0,0))

cv2.imshow("fINAL",final)
cv2.imwrite(f'{folder}/offset.png',final)
cv2.waitKey(0)