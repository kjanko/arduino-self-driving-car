import cv2
import os
import glob
from PIL import Image
import numpy as np
import cPickle

originalPath = "C:\\Users\\kjanko\\Desktop\\train_pics\\original"
writePath = "C:\\Users\\kjanko\\Desktop\\train_pics\\model.txt"

matrix = []
classes = []

for path in glob.glob(originalPath + "/*.jpg"):
	img = Image.open(path)
	img = img.convert('RGB')
	arr = []
	for x in range(0, 176):
		for y in range(0, 144):
			pixelRGB = img.getpixel((x,y))
			R,G,B = pixelRGB 
			brightness = sum([R,G,B])/3
			arr.append(brightness)
	arr = np.array(arr)
	matrix.append(arr)
	img_class = path.split("\\")[-1].split("_")[-1].split(".")[0]
	classes.append(img_class)
	
x = np.array(matrix)
y = np.array(classes)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(64,), random_state=1)
clf.fit(x, y)
f = open(writePath, "wb")
f.write(cPickle.dumps(clf))
f.close()


