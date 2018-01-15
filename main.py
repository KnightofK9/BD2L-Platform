from videoprocess import *
from videoprocesshandle import VideoProcessHandle

from random import randint

# Dummy key id
frame_ids = []
min_id = randint(0, 100)
max_id = randint(200, 250)
for i in range(min_id, max_id):
    frame_ids.append(i)
handle = VideoProcessHandle(frame_ids)
VideoProcess.process_video("input.avi", handle)
