import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import dumps
import speech_recognition as sr
from gtts import gTTS

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

            r = sr.Recognizer()
            with sr.AudioFile('index/static/index/media/audio.wav') as source:
                audio_data = r.record(source)
                request = r.recognize_google(audio_data, language="ru-RU")
                
                response = gTTS(text=request, lang="ru", slow=False)
                response.save("answer.wav")


    return JsonResponse({'message': 'Audio received and saved successfully.'})





