from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    # 使用render()函数
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('newapp/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, "newapp/index.html", context)


    # 使用template模板技术
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('newapp/index.html')
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    # return HttpResponse(template.render(context, request))

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("娇娇酱，我亲爱的宝贝！！！")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'newapp/detail.html', {'question': question})

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist111")
    # return render(request, 'newpolls/detail.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "newpolls/detail.html", {
            "question": question,
            "error_message": "You didni't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("newapp: results", args=(question.id,)))



