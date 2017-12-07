from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
    # q_obj = Question.objects.get(id=question_id)
    q_obj = get_object_or_404(Question, pk=question_id)  # Note: When we use this function we get 'Not Found: The requested URL /polls/3/ was not found on this server' when URL doesn't exists.
    context = {"question_obj": q_obj}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    return HttpResponse("Results for Question #%s are: " % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on Question #%s" % question_id)
