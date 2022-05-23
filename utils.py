from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np

class Block:
	def __init__(self, vid, pos, x, y, debug=False):
		self.vid = vid
		self.pos = pos
		self.x = x
		self.y = y
		xpos = int(pos[0])
		ypos = int(pos[1])

		self.num_frames = vid.shape[0]
		self.block = vid[:self.num_frames, ypos:ypos+y, xpos:xpos+x]
		self.shape = self.block.shape

		if debug:
			figure, ax = plt.subplots(1)
			rect = patches.Rectangle(pos, x, y, edgecolor='r', facecolor='none')
			ax.imshow(self.block[1, :ypos+y, :xpos+x, 0])
			ax.add_patch(rect)
	
	def blockavg(self, mult=1):
		blockavgs = np.empty(self.num_frames)
		for i in range(self.num_frames):
			frame = self.block[i]
			avg_frame = mult*np.sum(frame)/(self.x*self.y)
			blockavgs[i] = avg_frame
		return blockavgs

def reduce_array(array, accuracy = 0):
	reduced = []
	prev = -1
	for i in range(len(array)):
		rounded = round(array[i], accuracy)
		if rounded != prev:
			prev = rounded
			reduced.append(rounded)
	
	return reduced
def leftrise(framelist, index):
	if index == 0:
		rise = None
	else:
		rise = framelist[index] - framelist[index-1]
	return rise

def rightrise(framelist, index):
	try:
		rise = framelist[index+1] - framelist[index]
	except IndexError:
		rise = None
	return rise

def count_extrema(array, threshold=0):
	extrema = 0
	for i in range(len(array)):
		lrise = leftrise(array, i)
		rrise = rightrise(array, i)

		if lrise and rrise:
			if abs(lrise) < threshold and abs(rrise) < threshold:
				continue
			if lrise/abs(lrise) == -rrise/abs(rrise):
				extrema+=1
		else:
			extrema += 1
	
	return extrema

