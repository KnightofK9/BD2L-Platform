import cv2


class VideoProcess:
    def __init__(self):
        pass

    @staticmethod
    def process_video(input_path, handle):
        count = 0
        video = cv2.VideoCapture(input_path)
        success, image = video.read()
        if not success:
            print "Read video failed!"
            return
        handle.on_video_loaded(video)
        while success:
            handle.on_receive_frame(count, image)
            count += 1
            success, image = video.read()
        print "Read video completed!"
        handle.on_video_completed()
        video.release()
