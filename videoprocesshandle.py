# -*- coding: utf-8 -*-
import cv2
from random import randint


class VideoProcessHandle:
    def __init__(self, key_frame_list):
        # Width of input video
        self.input_width = 0
        # Height of input video
        self.input_height = 0
        # sign_id and it's meaning
        self.name_of_sign_id_dict = {
            "1": "Bien dung",
            "2": "Bien re trai",
            "3": "Bien re phai",
            "4": "Bien cam re trai",
            "5": "Bien cam re phai",
            "6": "Bien mot chieu",
            "7": "Bien toc đo toi da",
            "8": "Cac loai bien khac"
        }
        # Key frame list
        self.key_frame_list = key_frame_list
        # Array hold all detected obj info
        self.detected_obj_list = []
        # Output video in XVID
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
        obj = {"left": left, "right": right, "top": top, "bottom": bottom, "sign_id": sign_id}
        is_object_found = True
        # End data
        if is_object_found:
            self.on_object_found(obj["left"], obj["top"], obj["right"], obj["bottom"], obj["sign_id"], image, frame_id)
        self.out.write(image)

    def on_video_loaded(self, video):
        (major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')
        if int(major_ver) < 3:
            input_width = video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
            input_height = video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        else:
            input_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
            input_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.input_width = input_width
        self.input_height = input_height

    def is_frame_accepted(self, frame_id, image):
        # return True if you want to process all frame
        # return True
        return frame_id in self.key_frame_list

    def on_object_found(self, left, top, right, bottom, sign_id, image, frame_id):
        self.draw_rect_on_image(image, left, top, right, bottom)
        self.draw_text_on_image(image, sign_id)
        self.save_detected_obj_info(frame_id, sign_id, left, top, right, bottom)

    def draw_text_on_image(self, image, sign_id):
        font = cv2.FONT_HERSHEY_SIMPLEX
        name = self.get_name_of_sign_id(sign_id)
        left = int(self.input_width * 0)
        top = int(self.input_height * 0.7)

        cv2.putText(image, name, (left, top), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

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

    def get_name_of_sign_id(self, sign_id):
        return self.name_of_sign_id_dict[str(sign_id)]
