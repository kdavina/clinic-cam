from bluedot import BlueDot
from picamera import PiCamera
import time
import os

# This is the magic of git!


def take_picture():
    global last_video_pic
    global started_video
    global recent_ended_video
    print("started_video:", started_video)
    print("recent_ended_video:", recent_ended_video)
    if not started_video:
        if recent_ended_video:
            print("Entered if 1")
            recent_ended_video = False
        else:
            print("Entered else 1")
            last_video_pic = '/home/pi/Pictures/image_' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'
            cam.capture(last_video_pic)
            print("picture captured")


def stop_program(swipe):
    global continue_program
    if swipe.distance >= 2:
        cam.stop_preview()
        continue_program = False
        bd.stop()
    else:
        continue_program = True
        print("continue_program", continue_program)


def record_video():
    global started_video
    global last_video_pic
    global recent_ended_video
    if os.path.isfile(last_video_pic):
        os.remove(last_video_pic)
    if started_video:
        cam.stop_recording()
        started_video = False
        recent_ended_video = True
        print("stopped video. started_video=", started_video)
    else:
        cam.start_recording('/home/pi/Videos/video_' + time.strftime("%Y-%m-%d_%H-%M-%S") + '.h264')
        started_video = True
        print("started video. started_video=", started_video)


bd = BlueDot()
cam = PiCamera()
cam.start_preview()
started_video = False
last_video_pic = ''
recent_ended_video = False
bd.when_double_pressed = record_video
bd.set_when_pressed(take_picture, background=True)
bd.when_swiped = stop_program





