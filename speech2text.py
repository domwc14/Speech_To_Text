# import sounddevice as sd
# from scipy.io.wavfile import write

# fs = 44100  # Sample rate
# seconds = 3  # Duration of recording

# print('hello')
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file pip install write

from whisper_mic import WhisperMic

mic = WhisperMic()
result = mic.listen_loop()
print(result)