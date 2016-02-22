# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt

def main():
    wf = wave.open("test.wav" , "r" )
    buf = wf.readframes(wf.getnframes())
    # バイナリデータを16bit整数に変換
    data = np.frombuffer(buf, dtype="int16")
    plt.plot(data)
    plt.show()          # グラフ表示

if __name__ == '__main__':
    main()
