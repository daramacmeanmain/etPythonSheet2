#Problem Sheet - MNIST Data Files

import gzip
import PIL.Image as pil
import numpy as np
import uuid

#Part 1

def read_labels_from_file(filename):
	with gzip.open(filename, 'rb') as f:
		magic = f.read(4)
		magic = int.from_bytes(magic, 'big')
		print("Magic is:", magic)
		
		nolab = f.read(4)
		nolab = int.from_bytes(nolab, 'big')
		print("Number of labels:", nolab)
		
		labels = [f.read(1) for i in range(nolab)]
		labels = [int.from_bytes(label, 'big')for label in labels]
		
	return labels
	
train_labels = read_labels_from_file('train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('t10k-labels-idx1-ubyte.gz')

#Part 2

def read_images_from_file(filename):
	with gzip.open(filename, 'rb') as f:
		magic = f.read(4)
		magic = int.from_bytes(magic, 'big')
		print("Magic is:", magic)
		
		noimg = f.read(4)
		noimg = int.from_bytes(noimg, 'big')
		print("Number of images:", noimg)
		
		norow = f.read(4)
		norow = int.from_bytes(norow, 'big')
		print("Number of rows:", norow)
		
		nocol = f.read(4)
		nocol = int.from_bytes(nocol, 'big')
		print("Number of columns:", nocol)
		
		images = []
		
		for i in range(noimg):
			rows = []
			for r in range(norow):
				cols = []
				for c in range(nocol):
					cols.append(int.from_bytes(f.read(1), 'big'))
				rows.append(cols)
			images.append(rows)
	return images
	
train_images = read_images_from_file('train-images-idx3-ubyte.gz')
test_images = read_images_from_file('t10k-images-idx3-ubyte.gz')

for row in train_images[4999]:
	for col in row:
		print('.' if col <= 127 else '#', end='')
	print()
	
#Part 3

#Code for generating a unique filename adapted from https://stackoverflow.com/questions/2961509/python-how-to-create-a-unique-file-name
uf = str(uuid.uuid4())

img = train_images[4999]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
img.save(uf + '.png')