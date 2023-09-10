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
#test
            r = sr.Recognizer()
            with sr.AudioFile('index/static/index/media/audio.wav') as source:
                audio_data = r.record(source)
                request = r.recognize_google(audio_data, language="ru-RU")
                
                response = gTTS(text=request, lang="ru", slow=False)
                response.save("answer.wav")


    return JsonResponse({'message': 'Audio received and saved successfully.'})

# from transformers import pipeline
# from transformers import AutoTokenizer, AutoModelForCausalLM
#
#
#
# def remove_duplicate_words(input_str):
#     words = input_str.split()  # Разбиваем строку на слова
#     unique_words = []  # Здесь будем хранить уникальные слова
#     for word in words:
#         if word not in unique_words:
#             unique_words.append(word)
#     return ' '.join(unique_words)
# # Load model directly
# prompt = 'при включении тумблера топливный насос вал топливоподкачивающего агрегата не вращается.контактор ктн не включается'
#
# tokenizer = AutoTokenizer.from_pretrained("arsenZabara/RJD-hak", Legacy=True)
# model = AutoModelForCausalLM.from_pretrained("arsenZabara/RJD-hak")
#
# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=200)
# result = pipe(f"{prompt}")
#
# temp = result[0]['generated_text'].replace(prompt, '').replace('.', ' ')
# res = remove_duplicate_words((temp))
#
# print(res)





