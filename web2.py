import cv2
import time


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Получить информацию о размере кадра с помощью метода get()
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width,frame_height)
fps = 25
len_clip = 3  #длина клипов в минутах
tm = 0
color_yellow = (0,255,255)
with open("config", "r") as file:
    num_clip = int(file.read())
    

while cap.isOpened():
    curr_time = time.strftime("%d/%m/%y  %H:%M:%S", time.localtime())
    if tm:
        tm -= 1
        ret, img = cap.read()
        cv2.putText(img, f"FatherAppCam 1.05 {curr_time}", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_yellow, 1)
        cv2.imshow("camera", img)
        if ret == True:
            output.write(img)
        else:
            print("Поток отключен")
            break
        if cv2.waitKey(10) == 27: # Клавиша Esc
            break
    else: #блок создания новых записей, контроль з авременем
        try:
            if output.isOpened():
                print(f"закрыли cam{num_clip}")
                output.release()
        except: print("not output")
        finally:
            print("в финали зашли")
            
            num_clip += 1
            tm = fps*60*len_clip
            output = cv2.VideoWriter(f'rec{num_clip}.mp4', cv2.VideoWriter_fourcc(* 'mp4v'),fps,frame_size)
            if num_clip == 1440:
                num_clip = 0

with open("config","w") as fl:
    print(num_clip, file=fl)

output.release()

cap.release()
cv2.destroyAllWindows()