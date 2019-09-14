from transform_to_ascii import runner
from catch_frames import catch_video_frames
from terminal_viewer import show_frame_in_terminal

frames_list = list()
my_vid = str(input('Enter your video path: '))
my_vid = my_vid.replace('\\', '/')

for frame in catch_video_frames(my_vid):
    show_frame_in_terminal(runner(frame))

end = str(input('Press enter to Exit!'))
