# -*- coding: utf-8 -*-
import wave
import numpy as np
import struct
import matplotlib.pyplot as plt

# 波形の生成(振幅, 基本周波数, サンプリング周波数, 再生時間[s])
def create_wave(A, f0, fs, t):
    data = []
    # サンプル毎に計算
    for n in np.arange(t * fs):
        y = 0.0
        # サイン波(300個)の重ね合わせ
        for k in xrange(1,300):
            y += (A / k) * np.sin(2 * np.pi * k * f0 * n / fs)
        # 振幅を-1～1の範囲内に
        if y > 1.0:  y = 1.0
        if y < -1.0: y = -1.0
        data.append(y)

    return data

def main():
    data = create_wave(0.5, 261.63, 5000, 1)   # 波形の作成
    plt.plot(data)
    plt.xlim([0, 100])
    plt.show()

if __name__ == '__main__':
    main()
