import speech_recognition as sr
import Config

# для справки:
# https://cyberguru.tech/программирование/машинное-обучение/окончательное-руководство-по-распоз
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
# требуется установить PyAudio через pipwin

r = sr.Recognizer()         # инициализируем класс для распознования
mic = sr.Microphone()       # Получаем микрофон

print("Говорите...")
with mic as source:
    r.adjust_for_ambient_noise(source)  # Очистка звука от шумов
    audio = r.listen(source)            # записываем микрофон

print("Идёт распознание речи")
# распознаём речь
print(r.recognize_google(audio, language=Config.SpeechRecognitionLanguage))