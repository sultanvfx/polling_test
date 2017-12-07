
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index_page"),  # 127.0.0.1:8006/polls
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail_page"),  # 127.0.0.1:8006/polls/1
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="result_page"),  # 127.0.0.1:8006/polls/1/result
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote_page"),  # 127.0.0.1:8006/polls/1/vote
]

