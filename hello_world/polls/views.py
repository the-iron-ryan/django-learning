from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

def index(request):
    # building question list model
    latest_question_lis = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_lis,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objcets.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You're voting on question %s"
    return HttpResponse(response % question_id)
