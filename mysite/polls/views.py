from django.http import HttpResponse
from .models import *
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'first_question': latest_question_list[0]}
    return render(request, 'polls/index.html', context)

def some_url(request):
    return HttpResponse("some url를 구현해 봤습니다.")