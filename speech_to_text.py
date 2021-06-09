import speech_recognition as sr

r2 = sr.Recognizer()
with sr.Microphone() as source:
    print("\nTry Speaking")
    audio = r2.listen(source)

    try:
        text = r2.recognize_google(audio)
        print(f"You tried to speak this: {text}")
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))