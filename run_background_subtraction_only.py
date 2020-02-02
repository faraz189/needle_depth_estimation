import argparse

import cv2

from src.background_subtraction import BackgroundSubstraction


def parse_args():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('video_filename', type=str,
                         help='Path to the video file')
    _parser.add_argument('--process_frames', '-p', required=False, type=int, default=-1, dest='process_frames',
                         help='Specify the number of frames to process in the videos.')
    _parser.add_argument('--background_subtraction_type', '-b', required=False,
                         default='KNN', choices=['KNN', 'MOG'], dest='bg_type',
                         help='Specify the type of the background subtraction algorithm.')
    _args = vars(_parser.parse_args())
    return _args


def main():
    input_args = parse_args()
    bg_sub = BackgroundSubstraction(video_filename=input_args['video_filename'],
                                    background_substractor_type=input_args['bg_type'])
    _process_frames = input_args['process_frames'] if input_args['process_frames'] > 0 else int(1e10)
    for count in range(_process_frames):
        input_frame, fg_mask = bg_sub.run()  # auto-increments video file
        if fg_mask is None:
            print('End of video reached.')
            break
        cv2.imshow('bg_sub = {}'.format(input_args['bg_type']), fg_mask)
        cv2.imshow('frame', input_frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
