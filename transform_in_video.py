import cv2
import numpy


def convert_to_opencv(frame):
    opencv_image = numpy.array(frame)
    opencv_image = opencv_image[:, :, ::-1].copy() # RGB to BGR
    return opencv_image

def create_video_from_frames(frames_list, original_video):
    video_fps = cv2.VideoCapture(original_video)
    video_fps = video_fps.get(cv2.CAP_PROP_FPS)

    video_name = 'Asciified_' + original_video.split('/')[-1].split('.')[0] + '.mp4'

    force_mp4 = cv2.VideoWriter_fourcc(*'MP4')    
    video = cv2.VideoWriter(video_name, force_mp4, video_fps, (610, 850))

    for frame in frames_list:
        video.write(convert_to_opencv(frame))

    cv2.destroyAllWindows()
    video.release()
