from bluedot import BlueDot
from picamera import PiCamera
import time
import os

# This is the magic of git!

def take_picture():
    global last_video_pic
    last_video_pic = '/home/pi/Pictures/image_' + time.strftime('%Y-%m-%d....') + '.jpg'
    cam.capture(".jpg")

def stop_program():
    cam.stop_preview()
    global continue_program
    continue_program = False
    bd.stop()
    print("continue_program", continue_program)

def record_video():
    global started_video
    global last_video_pic
    os.remove(last_video_pic)
    if started_video:
        cam.stop_recording()
        started_video = False
        print("stopped video. started_video=", started_video)
    else:
        cam.start_recording('name_of_your_video.h264')
        print("started video. started_video=", started_video)

bd = BlueDot()
cam = PiCamera()
cam.start_preview()
started_video = False
last_video_pic = ''
bd.when_double_pressed = record_video
bd.set_when_pressed(take_picture, background=True)
bd.when_swiped = stop_program





