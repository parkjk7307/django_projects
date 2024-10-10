from django.http import HttpResponse
from .models import *
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    # context = {'first_question': latest_question_list[0]}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse(f"입력받은 id: {question_id}")

def some_url(request):
    return HttpResponse("some url를 구현해 봤습니다.")