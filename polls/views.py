from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from models import Question


def index(request):
    return HttpResponse("Welcome to the Landing Page !!!")


def detail(request, question_id):
    return HttpResponse("Detail description of the Question #%s is:" % question_id)


def results(request, question_id):
    return HttpResponse("Results for Question #%s are: " % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on Question #%s" % question_id)
