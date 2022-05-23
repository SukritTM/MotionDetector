# .....IDEA FOR LATER.....
# Maybe look at all the blocks?
# And compare adjacent blocks somehow?

import skvideo
import numpy as np
from matplotlib import pyplot as plt
import os
from skvideo import io
from skvideo import utils
import utils
import time

# load video
cwd = os.getcwd()
PATH_TO_FFMPEG = os.path.join(cwd, 'ffmpeg')
cwd = os.path.dirname(cwd)
PATH_TO_IO = os.path.join(cwd, 'output')

skvideo.setFFmpegPath(PATH_TO_FFMPEG)

def run(vidpath, filename):
	video = io.vread(vidpath, as_grey=True)
	num_frames = video.shape[0]
	y = video.shape[1]
	x = video.shape[2]

	larm = utils.Block(video, (2*x/3, y/2), 40, 40)
	rarm = utils.Block(video, (1.3*x/3, y/2), 40, 40)
	avg_frames_larm = larm.blockavg()
	avg_frames_rarm = rarm.blockavg()

	reduced_avg_frames_larm = utils.reduce_array(avg_frames_larm, 0)
	reduced_avg_frames_rarm = utils.reduce_array(avg_frames_rarm, 0)

	extrema_count_larm = utils.count_extrema(reduced_avg_frames_larm, 2.5)
	extrema_count_rarm = utils.count_extrema(reduced_avg_frames_rarm, 2.5)
	print('left arm extrema: ', extrema_count_larm)
	print('right arm extrema: ', extrema_count_rarm)

	if extrema_count_larm % 2 == 0:
		reps_larm = extrema_count_larm/4
	else:
		reps_larm = (extrema_count_larm-1)/4
	
	if extrema_count_rarm % 2 == 0:
		reps_rarm = extrema_count_rarm/4
	else:
		reps_rarm = (extrema_count_rarm-1)/4

	print('left arm reps:', reps_larm)
	print('right arm reps:', reps_rarm)

	if np.std(avg_frames_larm) > np.std(avg_frames_rarm):
		reps = reps_larm
	else:
		reps = reps_rarm

	print('avg reps:', reps)

	outputfile = open(PATH_TO_IO+f'/{filename}.txt', 'w')
	outputfile.write(f'{int(reps)}')
	outputfile.close()

while True:
	time.sleep(1)
	files = os.listdir(PATH_TO_IO)
	if files:
		for file in files:
			name, ext = file.split('.')
			if ext == 'mp4':
				run(os.path.join(PATH_TO_IO, file), name)
				os.remove(os.path.join(PATH_TO_IO, file))