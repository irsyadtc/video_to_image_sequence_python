import cv2
import os

print('extracting images and frame rates')

cap = cv2.VideoCapture('carem_office_230419.mp4')	#Change to your desired video

main_dir = r'/home/irsyad2/python/video_to_sequence/dataset' #Change to your desired output path
image_dir = r'/home/irsyad2/python/video_to_sequence/dataset/image_0'
time_dir = r'/home/irsyad2/python/video_to_sequence/dataset'

fps = cap.get(cv2.CAP_PROP_FPS)	#frame rate does not change in video?
timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]	#current frame timestamp

count = 0

#save directory
if not(os.path.exists(image_dir)):
	os.mkdir(main_dir)
	os.mkdir(image_dir)
os.chdir(image_dir)

print('saving frame images...')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))	#append current position of video in ms
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grayscale
        zero = ''
        millions = 100000
        while(count < millions):
        	zero = zero + "0"
        	millions = millions/10
        	if (millions <= 1):	#if equal or below ones decimal place
        		break
        cv2.imwrite(zero + str(count)+".jpg", grayscale)	#saving image
    
        print('timestamps: ',timestamps[-1])
        count = count + 1
    else:
        break

cap.release()


#write timestamp to file
print('Images saved. Generate times.txt...')
os.chdir(time_dir)
f = open("times.txt", "a")
for i, ts in enumerate(timestamps):	
	f.write(str(ts/1000) + "\n")
f.close()

print('Process ends')

#for i, ts in enumerate(timestamps):
#	print('fps: ', _fps)
#	print('timestamps: ',ts, '  calc_timestamps: ', cts)
#	print('Frame %d difference:'%i, abs(ts - cts))

