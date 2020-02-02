import cv2

from src.base_classes import BaseVideoOperation


class BackgroundSubstraction(BaseVideoOperation):
    def __init__(self, background_substractor_type=None, **kwargs):
        super().__init__(**kwargs)
        # self.video implemented in BaseClass
        if background_substractor_type == 'MOG':
            self.background_subtractor = cv2.createBackgroundSubtractorMOG2()
        elif background_substractor_type == 'KNN':
            self.background_subtractor = cv2.createBackgroundSubtractorKNN()
        else:
            raise ValueError('Provided Type {} is not supported. Please provide from list = [\'KNN\', \'MOG\'')

    def run(self, input_frame=None):
        if not input_frame and self.video:
            is_next_frame_available, input_frame = self.video.get_next_frame()
            if not is_next_frame_available:
                return None, None
        else:
            raise IOError('Error with video source.')
        fg_mask = self.background_subtractor.apply(input_frame)
        return input_frame, fg_mask
