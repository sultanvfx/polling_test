from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
    q_obj = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question_obj": q_obj})


def vote(request, question_id):
    q_obj = get_object_or_404(Question, pk=question_id)
    try:
        # Check whether any data is passed in request.POST & if not then tell User to select a Choice as done in the except clause.
        # Note: request.POST returns a dictionary-type object by which you can access submitted data by key name, here 'choice'
        selected_choice = q_obj.choice_set.get(pk=request.POST["choice"])
    except:
        return render(request, 'polls/detail.html', {"question_obj": q_obj, 'error_message': 'Please select a choice.'})

    else:  # else gets execute when try is successful
        selected_choice.votes_int += 1
        selected_choice.save()
    # Now show the results page.
    # Note: Instead of passing hard coded path as '/polls/1/results.html', we use the results.html page's name which is "result_page" and we pass the question.id value.
    # Very Important: Do add a comma in the end of args parameter as done below.
    return HttpResponseRedirect(reverse('polls_namespace:result_page', args=(q_obj.id, )))

