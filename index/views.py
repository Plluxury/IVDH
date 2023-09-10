import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import dumps
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
from django.http import JsonResponse
from .nlp import generate_text
import os
def index(request):
    return render(request, 'index/index.html')

@csrf_exempt
def audio(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('voice')
        if audio_file:
            # Process or save the audio file as needed.
            # For example, you can save it to a specific location:
            with open('index/static/index/media/audio.wav', 'wb') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            input_audio_file = 'index/static/index/media/audio.wav'  # problem
            audiosegment = AudioSegment.from_file(input_audio_file)

            audiosegment.export('index/static/index/media/output.wav', format='wav')

            with sr.AudioFile('index/static/index/media/output.wav') as source:
                r = sr.Recognizer()  # problem
                audio_data = r.record(source)
                inp = r.recognize_google(audio_data, language="ru-RU")
                print(inp)

                input_after_model = generate_text(inp)
                print(input_after_model)

                output = gTTS(text=input_after_model, lang="ru", slow=False)
                output.save("index/static/index/media/answer.wav")
                os.system("start answer.wav")

    return JsonResponse({'message': 'Audio received and saved successfully.'})








