
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404,render
# import template 
from django.template import loader

# import local model
from .models import Question

#### index ####
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # get pasific templet
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    print(context)
    return HttpResponse(template.render(context, request))

# # Use render
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

####detail####
## Call render to do 
# def detail(request, question_id):
#     try:
#         question = Question.object().get(pk=question_id)
#     except:
#         raise Http404('Question does not exit')
#     return render(request,'polls/detail.html',{"question":question})

# Use short
def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{"question":question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


