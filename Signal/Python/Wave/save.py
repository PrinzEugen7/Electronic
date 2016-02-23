# -*- coding: utf-8 -*-
import wave
import numpy as np
import struct

# 波形の生成(振幅, 基本周波数, サンプリング周波数, 再生時間[s])
def create_wave(A, f0, fs, t):
    data = []
    for n in np.arange(t * fs):
        s = A * np.sin(2 * np.pi * f0 * n / fs) # 正弦波の計算
        # 振幅の範囲を-1～1に設定
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)

    data = [int(x * 32767.0) for x in data]    # [-32768, 32767]の整数値に変換
    data = struct.pack("h" * len(data), *data) # バイナリデータに変換
    return data

# 波形データを保存(波形データ, ビット数, サンプリング周波数, ファイル名)
def save_wave(data, bit, fs, filename):
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit / 8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()

def main():
    fs = [261.63, 293.66, 329.63, 349.23]   # ドレミファの周波数[Hz]
    datas=""
    for f in fs:
        data = create_wave(1, f, 5000, 1)   # 波形の作成
        datas += data
    save_wave(datas, 5000, 16, "test.wav")  # 波形データをwavファイルで保存

if __name__ == '__main__':
    main()
