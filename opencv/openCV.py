#coding: utf-8
import cv2

cap0 = cv2.VideoCapture(0)

fps = cap0.get(cv2.CAP_PROP_FPS)

w = cap0.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap0.get(cv2.CAP_PROP_FRAME_HEIGHT)

print (fps,'(fps)')
print (w, '*',h)

while True:
    (ret, frame) = cap0.read()
    if ret:
        cv2.imshow('Camera: 0',frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k ==67 or k == 99:
            cv2.imwrite('capture.png',frame,[cv2.IMWRITE_PNG_COMPRESSION,3])
    else:
        print('camera is not ready')

cap0.release()
cv2.destroyAllWindows()
