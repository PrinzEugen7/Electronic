# -*- coding: utf-8 -*-
import wave

def main():
    wf = wave.open("test.wav" , "r" )
    print"Channel:", wf.getnchannels()

if __name__ == '__main__':
    main()
