from catch_frames import catch_video_frames
from terminal_viewer import create_image_from_frame
from transform_in_video import create_video_from_frames
from transform_to_ascii import runner

frames_list = list()
my_vid = str(input('Enter your video path: '))
my_vid = my_vid.replace('\\', '/')

frame_id = 1
for frame in catch_video_frames(my_vid):
    new_frame = create_image_from_frame(runner(frame))
    frames_list.append(new_frame)

create_video_from_frames(frames_list, my_vid)

end = str(input('Press enter to Exit!'))
