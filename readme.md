 sudo docker build -t webcam .

sudo docker run -it --device /dev/video0 -v /data/cam:/data/cam webcam