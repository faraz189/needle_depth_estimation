import os

import cv2


class VideoFileAdapter:
    # Video adapter for getting frames from local storage.
    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise IOError('Video file was not found at location = {}'.format(filename))
        self.filename = filename
        self.video_capture = cv2.VideoCapture(filename)
        if not self.video_capture.isOpened():
            raise IOError('Video capture was not initialized due to some error.')

    def get_next_frame(self):
        return self.video_capture.read()

    def __del__(self):
        self.video_capture.release()
