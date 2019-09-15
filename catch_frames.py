import cv2


def catch_video_frames(video_path):

    vidcap = cv2.VideoCapture(video_path)
    success = True
    while success:
        try:
            success,image = vidcap.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except Exception:
            return None

        yield image
    return None
