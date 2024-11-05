import cv2
import time

#video ismi
video_name = "yasaklı reklam krd.mp4"

#video içe aktarma: capture, cap

cap = cv2.VideoCapture(video_name)

print("Genişlik",cap.get(3))
print("Yukseklik",cap.get(4)) #yukseklik bilgisi

if cap.isOpened() == False:
    print("Hata")
    
    
while True:
    ret, frame = cap.read()
    
    if ret == True:
    
        time.sleep(0.04) # uyarı kullanmaz isek çok hızlı akar
    
        cv2.imshow("Video",frame)
    else: 
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows() 