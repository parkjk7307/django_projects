from django.http import HttpResponse, HttpResponseRedirect #, Http404
from .models import *
from django.shortcuts import render, get_object_or_404
from django.urls import * 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    # context = {'first_question': latest_question_list[0]}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    
    # #에러의 처리
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse(f"입력받은 id: {question_id}")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #return render(request, 'polls/detail.html', {'question': question, 'error_message': '선택이 없습니다.'})
        return render(request, 'polls/detail.html', {'question': question, 'error_message': f"선택이 없습니다. id={request.POST['choice']}"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:index'))