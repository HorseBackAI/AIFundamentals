"""
Resize the given image into a specified height (size)
Usage: python resize_image.py filename 600
600: default height to be resized to
"""

import cv2
import os, glob
import ntpath
from termcolor import colored
import sys

filename = str(sys.argv[1])

HEIGHT_CEILING = 600
try: 
	HEIGHT_CEILING = int(sys.argv[2])
except IndexError:
	pass

# input_file_path = os.path.expanduser("~/Desktop/")
file = os.getcwd() + '/' + filename

# output_dir = os.getcwd() + '/Snapshots/'
# if not os.path.exists(output_dir):
# 	os.mkdir(output_dir)

image = cv2.imread(file)
# cv2.imshow("original", image)
# cv2.waitKey(0)

print("原图尺寸和文件大小:\t\t {}, \t{}".format(image.shape, os.stat(file).st_size))
# (height, width, depth)

resized = image

if image.shape[0] > HEIGHT_CEILING:
	# Calculate the ratio of the new image to the old image.
	# Limit the height ceiling as HEIGHT_CEILING pixels.
	r = HEIGHT_CEILING * 1.0 / image.shape[0] # image: matrix, so row(height), column(width)
	dim = (int(image.shape[1] * r), HEIGHT_CEILING) # dim: (width, height)
		 
	# perform the actual resizing of the image and show it
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	# cv2.imshow("resized", resized)
	# cv2.waitKey(0)

# Write output image
output_file = 'out_' + ntpath.basename(file)
cv2.imwrite(output_file, resized)

# Echo info.
text = colored("修改后图片尺寸和文件大小:\t {}, \t{}".format(
	resized.shape, os.stat(output_file).st_size), "green")
print(text)

	
	
