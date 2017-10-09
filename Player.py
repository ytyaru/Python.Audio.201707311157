import pyaudio
class Player:
    def __init__(self): self.__pyaudio = pyaudio.PyAudio()
    def __del__(self): self.Close()
    def Close(self): self.__pyaudio.terminate()
    # 16bitで量子化したPCM(WAV)データに対応
    # paFloat32, paInt32, paInt24, paInt16, paInt8, paUInt8, paCustomFormat
    def Play(self, data, format=pyaudio.paInt16, channels=1, rate=8000):
        stream = self.__pyaudio.open(format=format,
                        channels=channels,
                        rate=int(rate),
                        output=True)
#        self.__chunk_write(data)
        chunk = 1024
        sp = 0  # 再生位置ポインタ
        buffer = data[sp:sp+chunk]
        while buffer != '':
            stream.write(buffer)
            sp = sp + chunk
            buffer = data[sp:sp+chunk]
            
        stream.stop_stream()
        stream.close()
    """
    def __chunk_write(self, data, chunk=1024):
        sp = 0  # 再生位置
        buffer = data[sp:sp+chunk]
        while '' != buffer:
            stream.write(buffer)
            sp = sp + chunk
            buffer = data[sp:sp+chunk]
    """
