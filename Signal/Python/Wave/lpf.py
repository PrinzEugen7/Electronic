# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt
import struct

# waveファイルの読み込み
def load_wave(filename):
    wf = wave.open(filename , "r" )
    fs = wf.getnframes()
    g = wf.readframes(wf.getnframes())          # waveファイルの信号データをバイナリ型から整数型(1～-1)に変換
    g = np.frombuffer(g, dtype="int16")/32768.0 # 信号をバイナリデータに変換
    return g, fs                                # 信号データgとサンプリング周波数fsを返す

# 信号をwave形式で保存(信号, ビット数, サンプリング周波数, ファイル名)
def save_wave(g, bit, fs, filename):
    g = [int(v * 32767.0) for v in g]
    g = struct.pack("h" * len(g), *g)
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit / 8)
    wf.setframerate(fs)
    wf.writeframes(g)
    wf.close()

def sinc(x):
    if x == 0.0: return 1.0
    else: return np.sin(x) / x

# ローパスフィルタのフィルタ係数を計算(fe:エッジ周波数、delta:遷移帯域幅)
def lpf(fe, delta):
    N = round(3.1 / delta) - 1    # N+1が奇数になるように調整
    if (N + 1) % 2 == 0: N += 1
    N = int(N)
    # フィルタ係数を求める
    b = []
    for i in range(-N/2, N/2 + 1):
        b.append(2.0 * fe * sinc(2.0 * np.pi * fe * i))

    # ハニング窓関数をかける
    window = np.hanning(N + 1)
    for i in range(len(b)):
        b[i] *= window[i]
    return b

# FIRフィルタ(元信号, フィルタ係数)
def fir(g, b):
    gf = [0.0] * len(g)     # 出力信号
    N = len(b) - 1          # フィルタ係数の数
    for n in range(len(g)):
        for i in range(N):
            if n - i >= 0:
                gf[n] += b[i] * g[n-i]
    return gf

# グラフ表示
def disp_graph(g, gf):
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

def main():
    g, fs = load_wave("test.wav")   # waveファイルの読み込み
    b = lpf(100.0 / fs, 10.0 / fs)# LPFのフィルタ係数を計算
    gf = fir(g, b)                  # FIRフィルタ処理
    save_wave(gf, 16, fs, "fir.wav")# 出力信号を保存
    disp_graph(g, gf)               # 元信号とフィルタ処理後の信号をグラフに表示

if __name__ == '__main__':
    main()
