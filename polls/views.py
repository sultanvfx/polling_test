from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from models import Question


def index(request):
    latest_questions = Question.objects.order_by("-publish_date")[:5]  # get first 5 questions, ordered by publish_date & latest should come first in output & hence the hyphen sign.
    output = ', '.join(q.question_str for q in latest_questions)
    return HttpResponse("<h1>Welcome to the Landing Page !!!</h1><hr><h2>Below are the questions:</h2><br>%s" % output)


def detail(request, question_id):
    return HttpResponse("Detail description of the Question #%s is:" % question_id)


def results(request, question_id):
    return HttpResponse("Results for Question #%s are: " % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on Question #%s" % question_id)
