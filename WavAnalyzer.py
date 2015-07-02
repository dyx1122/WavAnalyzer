import wave, struct

waveFile = wave.open('audio.wav', 'r')

length = waveFile.getnframes()
for i in range(0,length):
    waveData = waveFile.readframes(1)
    # wave frame samples are stored in little endian**
    # this example works for a single channel 16-bit per sample encoding
    data = struct.unpack("<h", waveData)
    print int(data[0])