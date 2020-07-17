# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:12:16 2020

@author: TOSHIBA
"""

import os
import pydub
import glob
from pydub import AudioSegment
mp3_files=glob.glob('./*.mp3')

for mp3_file in mp3_files:
    wav_file=os.path.splitext(mp3_file)[0]+'.wav'
    sound=AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format='wav')
    os.remove(mp3_file)
print("okeeyy")    