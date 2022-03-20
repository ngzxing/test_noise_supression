import noisereduce as nr
from scipy.io import wavfile

def noise_sup(infile, outfile):
    
    rate, data = wavfile.read("C:\\Users\\user\Downloads\\"+infile)
    reduced_noise = nr.reduce_noise(y=data, sr=rate,prop_decrease=0.95)
    wavfile.write("C:\\Users\\user\Downloads\\"+outfile, rate, reduced_noise)
    
noise_sup("babble_15db.wav", "babbleReduced.wav")
