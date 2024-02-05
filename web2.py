import cv2
import time
import os


#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)
# Получить информацию о размере кадра с помощью метода get()
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width,frame_height)
fps = 25
len_clip = 3  #длина клипов в минутах
days_clip = 3
tm = 0
color_yellow = (0,255,255) 
sum_clip = days_clip*24*60/len_clip
folder_save_move = '/data/cam/'
conf = folder_save_move+'config'
if os.path.isfile(conf):
    with open(conf, "r") as file:
        num_clip = int(file.read())
else:
    num_clip=0
    

while cap.isOpened():
    curr_time = time.strftime("%d/%m/%y  %H:%M:%S", time.localtime())
    if tm:
        tm -= 1
        ret, img = cap.read()
        cv2.putText(img, f"FatherAppCam 1.05 {curr_time}", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_yellow, 1)
        if ret == True:
            output.write(img)
        else:
            print("Поток отключен")
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
            output = cv2.VideoWriter(f'{folder_save_move}rec{num_clip}.mp4', cv2.VideoWriter_fourcc(* 'mp4v'),fps,frame_size)
            if num_clip == sum_clip:
                num_clip = 0

            with open(conf,"w") as fl:
                print(f"запись в конфиг {num_clip}")
                print(num_clip, file=fl)

try:
    output.release()
except:
    print("камера не найдена")

cap.release()
cv2.destroyAllWindows()