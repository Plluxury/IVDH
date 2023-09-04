import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    return render(request, 'index/index.html')


@csrf_exempt
def audio(request):
    name = ''
    if request.POST:
        name = json.loads(request.body)

    return JsonResponse({'name': name})
