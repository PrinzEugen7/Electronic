# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt
import struct

# FIRフィルタ(元信号, フィルタ係数)
def fir(g, b):
    gf = [0.0] * len(g)     # フィルタの出力信号
    N = len(b) - 1          # フィルタ係数の数
    for n in range(len(g)):
        for i in range(N+1):
            if n - i >= 0:
                gf[n] += b[i] * g[n-i]
    return gf

def main():
    wf = wave.open("test.wav" , "r" )
    fs = wf.getnframes()
    # waveファイルの信号データをバイナリ型から整数型(1～-1)に変換
    g = wf.readframes(wf.getnframes())
    g = np.frombuffer(g, dtype="int16") / 32768.0
    # FIRフィルタ処理
    b = [0.5, 0.5]  # フィルタ係数
    gf = fir(g, b)  # FIRフィルタ処理

    # 信号の描画(フィルタ処理前)
    plt.subplot(211)
    plt.plot(g)
    plt.axis([0, 300, -1.0, 1.0])   # 表示する範囲
    plt.xlabel("Time [sample]")
    plt.ylabel("Amplitude")

    # 信号の描画(フィルタ処理後)
    plt.subplot(212)
    plt.plot(gf)
    plt.axis([0, 300, -1.0, 1.0])   # 表示する範囲
    plt.xlabel("time [sample]")
    plt.ylabel("Amplitude")
    plt.show()          # グラフ表示

if __name__ == '__main__':
    main()
