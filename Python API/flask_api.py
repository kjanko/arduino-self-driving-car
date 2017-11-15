#!flask/bin/python
from flask import Flask
from flask import request
import base64
from PIL import Image
import cv2

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    if not request.json or not 'encoded_string' in request.json:
        abort(400)
	
	image_string = request.form['encoded_string']
	img = base64.b64decode(image_string)
	# DONT ASK ME IT JUST WORKS THIS WAY
	filename = 'img.jpg'
	with open(filename, 'wb') as f:
		f.write(img)
		
	img = Image.open(filename)
	img = img.convert('RGB')
	img = cv2.resize(img, (176, 144), interpolation = cv2.INTER_CUBIC)
	img_arr = []
	for x in range(0, 176):
		for y in range(0, 144):
			pixelRGB = img.getpixel((x,y))
			R,G,B = pixelRGB 
			brightness = sum([R,G,B])/3
			img_arr.append(brightness)

	x = np.array(img_arr)
	
	#Load serialized model
	f = open("C:\\Users\\kjanko\\Desktop\\train_pics\\model.txt", "rb")
	clf = cPickle.load(f)
	f.close()
	
	return clf.predict(x)
	

@app.route('/')
def index():
    return "Hello, World!"
	

	

if __name__ == '__main__':
    app.run(debug=True)
