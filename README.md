Video to Image Sequence Converter
=========

This python3 code converts video to image sequence for creating dataset. It also generates times.txt file which logs the timestamps of the frames. The default directories of the output are similar to KITTI dataset folder used in ORB-SLAM2.


### How to use
1. Set the file to executable
```
chmod +x 4_video2framerate_2.py
```
2. Edit 4_video2framerate_2.py file as follows:

Set your video name in line 6

```
cap = cv2.VideoCapture('carem_office_230419.mp4')
```

Set your main path of your output at line 8

```
main_dir = r'/home/user/.../video_to_sequence_image_python/dataset'
```

Set your subpath of the images output 

```
image_dir = r'/home/user/.../video_to_sequence_image_python/dataset/image_0'
```

Set your subpath of the times.txt
```
time_dir = r'/home/user/.../video_to_sequence_image_python/dataset'
```
3. run the file in terminal
```
python3 4_video2framerate_2.py
```


