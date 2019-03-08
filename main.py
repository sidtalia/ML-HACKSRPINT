import cv2
import numpy as np 
import soundfile as sf 
import sounddevice as sd 
import time
from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import math as m 

layer_tensor = model.layer_tensors[3]


def conditioner(data):
	data *= 128
	data += 128
	data = np.array(data,dtype=np.uint8)
	return data

def process(img):
	img = recursive_optimize(layer_tensor=layer_tensor, image=img,
                 # how clear is the dream vs original image        
                 num_iterations=20, step_size=1.0, rescale_factor=0.5,
                 # How many "passes" over the data. More passes, the more granular the gradients will be.
                 num_repeats=6, blend=0.2)
	img -= (np.max(img)-np.min(img))/2
	img = np.clip(img, 0.0, 255.0)
	img = img.astype(np.uint8)
	return img

data, fs = sf.read('ODESZA - Loyal.wav', dtype='float32')

original_shape = data.shape
print(fs)
slot_size = ((fs//2)*3)
side = int(m.sqrt(fs))
slots = int(data.shape[0]/slot_size)
output = []

delay = np.array([1,1,2,3,5,8,13,21])
drop = np.zeros_like(delay)
for i in range(len(delay)):
	drop[i] = np.sum(delay[:i+1])+1
k=0 #initialize k as 0
print(drop)
offset = drop[-1]


data = conditioner(data)
data = data[:slots*slot_size]
for i in range(slots):
	a = data[i*slot_size:(i+1)*slot_size]
	orig = a = np.reshape(a,(side,side,3))
	cv2.imshow('original',a)
	if(drop[k]==i):
		k+=1
		ratio = (k/len(drop))**4
		if(k==len(drop)):
			drop+=offset
		k = k%len(drop)#ensure no out of bound answers
		a = process(a)
		kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
		a = cv2.filter2D(a,-1,kernel)
		a = (ratio*a)+((1-ratio)*orig)
	cv2.imshow('remix',a)
	output.append(a)
	ch = 0xFF & cv2.waitKey(5) #press ESC key to exit
	if ch == 27:
		break
cv2.destroyAllWindows()

out = np.array(output,dtype=np.float32)
out -= 128
out /= 128
out = np.reshape(out,data.shape)
np.save('test3.npy',out)
sf.write('stereo_file.wav', out, fs, 'PCM_24')
