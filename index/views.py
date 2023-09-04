import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



def index(request):
    return render(request, 'index/index.html')


@csrf_exempt
def audio(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/audioAPI/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, "name.html", {"form": form})



