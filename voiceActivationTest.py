import speech_recognition as sr
import time

import Config

# для справки
# https://github.com/Uberi/speech_recognition/blob/master/examples/background_listening.py

# инициализируем основные классы
r = sr.Recognizer()
m = sr.Microphone()

__isListening = True

# результат по определению
def callback(recognizer, audio):
    try:
        # получаем сказаное пользователем слово
        word = str(recognizer.recognize_google(audio, language=Config.SpeechRecognitionLanguage)).lower()
        print(word)
        # если слово есть то выходим из цикла и сворачиваем прослушку
        for ActivationPhrase in Config.ActivationPhrases: #TODO: Исправить провеку
            if ActivationPhrase in word:
                global __isListening
                __isListening = False
                break
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        pass
    '''
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")'''

# накладываем шумоподавленеи для микрофона
with m as source:
    r.adjust_for_ambient_noise(source)
# начинаем прослушивать пользователя асинхронно
stop_listening = r.listen_in_background(m, callback)

# зацикливаем программу чтобы она не вылетела
while __isListening:
    time.sleep(0.1)

stop_listening(wait_for_stop=__isListening)
print("Запуск основного блока Амадеуса")