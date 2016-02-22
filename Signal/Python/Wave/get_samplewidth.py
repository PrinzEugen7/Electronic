# -*- coding: utf-8 -*-
import wave

def main():
    wf = wave.open("test.wav" , "r" )
    print"Sample Width:", wf.getsampwidth()

if __name__ == '__main__':
    main()
