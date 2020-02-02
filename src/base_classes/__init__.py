from abc import ABC, abstractmethod

from src.VideoAdapters import VideoFileAdapter


class BaseVideoOperation(ABC):
    def __init__(self, **kwargs):
        self.video = self.get_video_source(kwargs)

    @staticmethod
    def get_video_source(kwargs):
        # Override this method to change the video adapter, in case of other video source
        if 'video_filename' in kwargs:
            return VideoFileAdapter(filename=kwargs['video_filename'])
        return None

    @abstractmethod
    def run(self):
        return NotImplemented
