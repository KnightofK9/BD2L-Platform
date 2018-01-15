from videoprocess import *
from videoprocesshandle import VideoProcessHandle

# Dummy key id
handle = VideoProcessHandle([12, 13, 14, 15, 16, 17, 24, 40, 100])
VideoProcess.process_video("input.avi", handle)
