from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader, RequestContext

# Create your views here.
from models import Question


def index(request):
    latest_questions = Question.objects.order_by("-publish_date")[:5]  # get first 5 questions, order by publish_date & latest should come first in output & hence the hyphen sign.
    # --- Either use the below 3 lines:
    # template = loader.get_template("polls/index.html")
    # context = RequestContext(request, {"latest_questions_list": latest_questions})
    # return HttpResponse(template.render(context))
    # --- Or use below code which is the shortcut:
    context = {"latest_questions_list": latest_questions}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("Detail description of the Question #%s is:" % question_id)


def results(request, question_id):
    return HttpResponse("Results for Question #%s are: " % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on Question #%s" % question_id)
