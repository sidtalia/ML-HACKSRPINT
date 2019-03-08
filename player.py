import numpy as np
import sounddevice as sd

data = np.load('test2.npy')
sd.play(data,44100,device=2)