import speech_recognition as sr 

r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(query)