# .....IDEA FOR LATER.....
# Maybe look at all the blocks?
# And compare adjacent blocks somehow?

import numpy as np
import os
from skvideo import io
from skvideo import utils
import utils

import sys

# load video
cwd = os.getcwd()
PATH_TO_IO = os.path.join(cwd, 'vid')


def run(vidpath):
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
	# print('left arm extrema: ', extrema_count_larm)
	# print('right arm extrema: ', extrema_count_rarm)

	if extrema_count_larm % 2 == 0:
		reps_larm = extrema_count_larm/4
	else:
		reps_larm = (extrema_count_larm-1)/4
	
	if extrema_count_rarm % 2 == 0:
		reps_rarm = extrema_count_rarm/4
	else:
		reps_rarm = (extrema_count_rarm-1)/4

	# print('left arm reps:', reps_larm)
	# print('right arm reps:', reps_rarm)

	if np.std(avg_frames_larm) > np.std(avg_frames_rarm):
		reps = reps_larm
	else:
		reps = reps_rarm

	# print('avg reps:', reps)

	return reps

if __name__ == '__main__':
	file = sys.argv[1]
	reps = run(os.path.join(PATH_TO_IO, file))
	print(reps)