import noisereduce as nr
from scipy.io import wavfile

def noise_sup(infile, outfile):
    
    rate, data = wavfile.read(infile)
    reduced_noise = nr.reduce_noise(y=data, sr=rate,prop_decrease=0.95)
    wavfile.write(outfile, rate, reduced_noise)
    

