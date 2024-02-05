```sudo mkdir -p --mode=777 /data/cam```
```cd /opt/```
```sudo git clone https://github.com/Atatanoff/videocam.git'''
```cd videocam```
```sudo docker build -t webcam .```

```sudo docker run -it --device /dev/video0 -v /data/cam:/data/cam webcam```