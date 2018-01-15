import cv2
from random import randint


class VideoProcessHandle:
    def __init__(self, key_frame_list):
        self.key_frame_list = key_frame_list
        self.detected_obj_list = []

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        pass

    def on_receive_frame(self, frame_id, image):
        if not self.is_frame_accepted(frame_id, image):
            self.out.write(image)
            return
        print "Processing frame {}".format(str(frame_id))
        # TODO: process all accepted frame here, found the top, left, right, bottom, sign_id and pass to on_object_found
        # Dummy data
        left = randint(0, 500)
        right = left + 100
        top = randint(0, 300)
        bottom = top + 100
        sign_id = 1
        # End data
        self.on_object_found(left, top, right, bottom, sign_id, image, frame_id)
        self.out.write(image)

    def is_frame_accepted(self, frame_id, image):
        # return true if you want to process all frame
        return frame_id in self.key_frame_list

    def on_object_found(self, left, top, right, bottom, sign_id, image, frame_id):
        self.draw_rect_on_image(image, left, top, right, bottom)
        self.save_detected_obj_info(frame_id, sign_id, left, top, right, bottom)

    def save_detected_obj_info(self, frame_id, sign_id, left, top, right, bottom):
        self.detected_obj_list.append([frame_id, sign_id, left, top, right, bottom])

    def save_output(self):
        output_file = open('output.txt', 'w')
        output_file.write(str(len(self.detected_obj_list)) + "\n")
        for obj in self.detected_obj_list:
            output_file.write(" ".join(map(str, obj)) + "\n")
        output_file.close()

    def on_video_completed(self):
        self.save_output()
        self.release_resource()
        return

    def release_resource(self):
        self.out.release()

    def draw_rect_on_image(self, image, left, top, right, bottom):
        cv2.rectangle(image, (top, left), (bottom, right), (0, 255, 0), 3)
