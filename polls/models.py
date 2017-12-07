from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Question(models.Model):
    question_str = models.CharField(max_length=200)
    publish_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_str


class Choice(models.Model):
    choice_str = models.CharField(max_length=200)
    votes_int = models.IntegerField()
    question_obj = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_str
