import argparse

import cv2

from src.optical_flow import OpticalFlow


def parse_args():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('video_filename', type=str,
                         help='Path to the video file')
    _parser.add_argument('--process_frames', '-p', required=False, type=int, default=-1, dest='process_frames',
                         help='Specify the number of frames to process in the videos.')
    _args = vars(_parser.parse_args())
    return _args


def main():
    input_args = parse_args()
    optical_flow_instance = OpticalFlow(video_filename=input_args['video_filename'])
    optical_generator = optical_flow_instance.run()
    _process_frames = input_args['process_frames'] if input_args['process_frames'] > 0 else int(1e10)
    for count in range(_process_frames):
        try:
            frame, frame_optical_density = next(optical_generator)
            _, _binary_optical_density = cv2.threshold(cv2.cvtColor(frame_optical_density, cv2.COLOR_BGR2GRAY), 10, 255,
                                                       cv2.THRESH_BINARY)
            cv2.imshow('optical_flow', _binary_optical_density)
            cv2.imshow('frame', frame)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        except StopIteration:
            print('Video end has reached.')
            break


if __name__ == '__main__':
    main()
