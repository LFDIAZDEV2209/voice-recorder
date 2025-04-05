import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import threading
import os

fs = 44100  
recording = []  
is_recording = True

def get_file_name():
    count = 1
    while os.path.exists(f"out_{count}.wav"):
        count += 1
    return f"out_{count}.wav"

def callback(indata, frames, time, status):
    if status:
        print(status)
    if is_recording:
        recording.append(indata.copy())  

def record_audio():
    global is_recording
    print("Grabando... Presiona ENTER para detener.")
    
    with sd.InputStream(samplerate=fs, channels=2, dtype='int16', callback=callback):
        while is_recording:
            sd.sleep(100)  

    print("Grabación detenida... Guardando archivo.")
    save_audio()

def save_audio():
    audio_array = np.concatenate(recording, axis=0) 
    fileName = get_file_name() 
    write(fileName, fs, audio_array)  
    print(f"Archivo guardado como {fileName}")

recording_thread = threading.Thread(target=record_audio)
recording_thread.start()

input()
is_recording = False  

recording_thread.join()
print("Finalizado.")
