from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    # template = loader.get_template('newapp/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'newpolls/index.html', context)
    # return HttpResponse(template.render(context, request))

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("娇娇酱，我亲爱的宝贝！！！")


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'newpolls/detail.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on quesion %s." % question_id)