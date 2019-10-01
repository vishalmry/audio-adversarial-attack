import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('adv-FM-1000.wav','r')
print ('Opening adv-FM-1000.wav, ran after 1000 iterations...')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print ('Just mono files')
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.show()
