from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    list = ('박도윤','윤정인','강윤서','유수화','박지영','전수현','이혜인','최진영','송주연','김세은','김도이')
    team = random.sample(list, 2)

    return render(request, 'result.html', {'team':team})
