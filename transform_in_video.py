import cv2
import numpy


def convert_to_opencv(frame):
    opencv_image = numpy.array(frame)
    opencv_image = opencv_image[:, :, ::-1].copy()
    return opencv_image

def create_video_from_frames(frames_list, original_video):
    video_fps = cv2.VideoCapture(original_video)
    video_fps = video_fps.get(cv2.CAP_PROP_FPS)

    video_name = 'Asciified_' + original_video.split('/')[-1]
    
    video = cv2.VideoWriter(video_name, 0, video_fps, (610, 850))

    for frame in frames_list:
        video.write(convert_to_opencv(frame))

    cv2.destroyAllWindows()
    video.release()
