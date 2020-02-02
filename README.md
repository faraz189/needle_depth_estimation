# Needle Depth Estimation Project

___
## Experiment 1: Optical Flow

The code runs the opencv implementation of the Lucas-Kanade optical flow algorithm on the video provided.

For running the code on video, that is stored on file.

``python run_optical_flow.py <path_to_video>``

For detailed explanation of the input arguments, please run 

``python run_optical_flow.py --help``

___
## Experiment 2: Background Subtraction

The code runs the opencv implementation of the Background Subtraction methods, KNN or MOG. [See Documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html "Opencv Documentation")

For running the code on video, stored on file system.

``python run_background_subtraction.py <path_to_video> -b [KNN, MOG]``

For detailed explanation of the input arguments, please run

``python run_background_subtraction.py --help``
