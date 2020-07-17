# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 04:00:25 2020

@author: TOSHIBA
"""

import os
import threading
from tkinter import *
from pygame import mixer
from tkinter import filedialog

#      DOSYADAN MÜZİK SEÇİMİ
sec = Tk()
sec.geometry('400x200')
sec.title("Müzik Seçimi")

foto_nota=PhotoImage(file="music-note.png")
labelfoto2=Label( image=foto_nota )
labelfoto2.pack(side=LEFT)


leftframe = Frame(sec)
leftframe.pack(side=LEFT, padx=30)


rightframe = Frame(sec)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()

r=[]

def file_al():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)


def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    r.insert(index, filename) #*******

text = Label(topframe, text='Dinlemek istediğiniz müzik')
text.pack()

def qu():
    global sec
    sec.destroy()

playlistbox = Listbox(topframe, width=20, height=2)
playlistbox.pack()

btn1=Button(topframe,text="müzik sec",command=file_al)
btn1.pack(pady=2)
btn2=Button(topframe,text="tamam", command=qu)
btn2.pack(pady=4)
sec.mainloop()



song=r[0]

#%%
import librosa
import pandas as pd
import numpy as np

import os
import csv
header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
for i in range(1, 21):
    header += f' mfcc{i}'
header += ' label'
header = header.split()

file = open('data_yeni.csv', 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)

songname = str(song)
y, sr = librosa.load(songname, mono=True, duration=30)
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
rmse = librosa.feature.rmse(y=y)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
to_append = f'{songname} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
for e in mfcc:
    to_append += f' {np.mean(e)}'
to_append += f' '
file = open('data_yeni.csv', 'a', newline='')
with file:
     writer = csv.writer(file)
     writer.writerow(to_append.split())
#%%     Alınan müziğin tahmini için modele verilmesi ve predict işlemi
from sklearn.externals import joblib
     
data_yeni=pd.read_csv("data_yeni.csv")     
data_yeni=data_yeni.drop("mfcc2", axis=1)
data_yeni=data_yeni.drop("filename", axis=1)

aa=data_yeni.drop("label", axis=1)
rfc = joblib.load('modell.pkl')
label_pred =int( (rfc.predict(aa)))
print(label_pred)
#print("the best price for this Dacia is",rfc.predict([a])[0])
data_yeni['label'].fillna(label_pred, inplace = True)
data7=pd.read_csv("yepyeni.csv")
data7=data7.drop("filename", axis=1)
data7=data7.drop("mfcc2", axis=1)
x=data7.drop('label',axis=1)
#%% string olan label değerlerini sayısal değere dönüştürdü
from sklearn.preprocessing import LabelEncoder
genre_list = data7.iloc[:, -1]
encoder = LabelEncoder()
data7.label = encoder.fit_transform(genre_list)
y=data7.label
data7 = data7.append(data_yeni, ignore_index=True)
#%%     label değerinin adını yazdırıyor
def numbers_to_strings(label_pred): 
    switcher = { 
        0: "blues", 
        1: "classical", 
        2: "electronic", 
        3: "hiphop",
        4: "metal", 
        5: "punk",
    } 
  
    return switcher.get(label_pred, "nothing") 
  
if __name__ == "__main__": 
    argument=0
    selam=numbers_to_strings(label_pred)
    print (numbers_to_strings(label_pred) )
#%%      COsine Similarrty
from sklearn.metrics.pairwise import cosine_similarity
cos_sim = cosine_similarity(data_yeni, data7).flatten()
#%%
dataaa=pd.read_csv("yepyeni.csv")
import pandas as pd
df = pd.DataFrame()
#df["music"]=df.index
df["simila"]=cos_sim
df["adi"]=dataaa.filename
df["label"]=data7.label

df.sort_values(by=['simila'], inplace=True, ascending=False)
oneri=df.head(7)
onerim=list(oneri.adi)
for t in onerim:
    r.append(t)
del(onerim[1])
#%%
del (r[1])
#%%
root = Tk()
mixer.init()
root.geometry('500x400')
root.title(" SY Music  ")
text1 = Label(root, text='Müzik Türünü Öğren ', fg="#d293a7",font=("bold", 16, ))
text1.pack()
text2 = Label(root, text=' Ve ', fg="#d293a7",font=("bold", 16, ))
text2.pack()
text3 = Label(root, text='Benzer Şarkıları Dinle', fg="#d293a7",font=("bold", 16, ))
text3.pack()


foto=PhotoImage(file="resim_song2.png")
labelfoto=Label( image=foto )
labelfoto.pack(side=RIGHT)

"""
import pandas as pd
data=pd.read_csv("yepyeni.csv")
aa=data.head(3)
b=aa.filename

#r=[]
for i in b:
    r.append(i)
"""

dosya="C:/Users/TOSHIBA/Desktop/tk/logo.png"
def play_btn():
    selected_song=lbl.curselection()
    selected_song=int(selected_song[0])
    print("secildi",selected_song)
    play_it=r[selected_song]
    print("çal",play_it)

    
    mixer.music.load(play_it)  # şarıkının adı
    mixer.music.play()
    print("çalışıyor")

def stop_music():
    mixer.music.stop()
    print("durdu")



middleframe = Frame(root)
middleframe.pack(padx=20,pady=20)


leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30)


rightframe = Frame(root)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()



#↨selamm=onerim[1]
label_tur = Label(topframe, text="sarkının türü:", fg="#84c2e1",font=("bold", 14, ))

label2 = Label(topframe, text=selam,  fg="#84c2e1",font=("bold", 12, ))
label_tur.pack()
label2.pack()

#c=b[0]

text_oneri=Label(leftframe, text="Dinlemek istediğin " "\n" "müzik ve öneriler")
text_oneri.pack()



lbl=Listbox(leftframe)
lbl.insert(0, r[0])
lbl.insert(1, r[2])
lbl.insert(2, r[3])
lbl.insert(3, r[4])
lbl.insert(4, r[5])
lbl.insert(5, r[6])

lbl.pack()


photo = PhotoImage(file="play-button.png")
btn = Button( image=photo, command=play_btn)
#btn.place(x=200,y=-150)
btn.pack(side=LEFT, padx=10)

stopPhoto=PhotoImage(file="stop.png")
stopBtn = Button( image=stopPhoto, command=stop_music)
#─stopBtn.place(x=150,y=-150)

stopBtn.pack(side=LEFT, padx=10)

root.mainloop()

