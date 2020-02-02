import cv2
import numpy as np

from src.background_subtraction import BackgroundSubstraction
from src.base_classes import BaseVideoOperation


class OpticalFlow(BaseVideoOperation):
    # Used code from
    # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
    __DEFAULT_SHI_TOMASI_PARAMS = {'maxCorners': 100, 'qualityLevel': 0.3,
                                   'minDistance': 7, 'blockSize': 7}
    __DEFAULT_LK_PARAMS = {'winSize': (15, 15), 'maxLevel': 2,
                           'criteria': (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)}

    def __init__(self, corner_detector_params=None, optical_flow_params=None, background_subtraction_type=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.corner_detector_params = corner_detector_params if corner_detector_params \
            else OpticalFlow.__DEFAULT_SHI_TOMASI_PARAMS
        self.optical_flow_params = optical_flow_params if optical_flow_params else OpticalFlow.__DEFAULT_LK_PARAMS
        if background_subtraction_type:
            self.back_sub = BackgroundSubstraction(background_substractor_type=background_subtraction_type)
        else:
            self.back_sub = None

        # self.video moved to the base class

    def run(self):
        ret, frame1 = self.video.get_next_frame()
        previous_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        if self.back_sub:
            previous_frame = self.back_sub.run(input_frame=frame1)
        hsv = np.zeros_like(frame1)
        hsv[..., 1] = 255

        while 1:
            ret, frame2 = self.video.get_next_frame()
            next_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            flow = cv2.calcOpticalFlowFarneback(previous_frame, next_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)

            mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            hsv[..., 0] = ang * 180 / np.pi / 2
            hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
            rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            previous_frame = next_frame
            yield frame2, rgb
