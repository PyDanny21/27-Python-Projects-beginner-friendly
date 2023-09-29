from vosk import Model, KaldiRecognizer
import json
import pyaudio
import pyttsx3

p=pyttsx3.init('sapi5')
voices=p.getProperty('voices')
p.setProperty('voice',voices[1].id)
p.setProperty('rate',190)
p.setProperty('volume',1.0)

def speak(audio):
    print('')
    p.say(audio)
    print(audio)
    p.runAndWait()

# Download vosk-model-small-en-us-0.15
# add it path
model=Model("W:\\Projects\\Projects\\vosk-model-small-en-us-0.15")
recognizer=KaldiRecognizer(model,16000)
mic=pyaudio.PyAudio()
stream=mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
while True:
    data=stream.read(4096,exception_on_overflow=False)
    if len(data)==0:
        break
    if recognizer.AcceptWaveform(data):
          rec=recognizer.Result()
          command=json.loads(rec)
          print(command['text'])

        #   if 'hello' in command['text']:
        #       stream.stop_stream()
        #       print('\t\t\t\t\t\t\t\t\t\t\t\t\t'+command['text'])
        #       speak('Hi sir, I am Py assist,your personal assistant')
        #       speak('How may i help you?')
        #       stream.start_stream()
        #       print('')
        #       print('Listening')
        #       print('')
