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

# 信号をwave形式で保存(波形データ, ビット数, サンプリング周波数, ファイル名)
def save_wave(data, bit, fs, filename):
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit / 8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()

def main():
    wf = wave.open("test.wav" , "r" )
    fs = wf.getnframes()
    # waveファイルの信号データをバイナリ型から整数型(1～-1)に変換
    g = wf.readframes(wf.getnframes())
    g = np.frombuffer(g, dtype="int16") / 32768.0
    # FIRフィルタ処理
    b = [0.3, 0.3]  # フィルタ係数
    gf = fir(g, b)  # FIRフィルタ処理
    # 信号をバイナリデータに変換
    gf = [int(v * 32767.0) for v in gf]
    gf = struct.pack("h" * len(gf), *gf)
    # フィルタ処理後の信号を保存
    save_wave(gf, 16, fs, "fir.wav")

if __name__ == '__main__':
    main()
