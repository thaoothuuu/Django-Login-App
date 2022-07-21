import datetime

from django.db import models

# Create your models here.
from django.db.models import Model


class Question(Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField(default=datetime.datetime.now().date())

    def __str__(self):
        return self.question_text


class Choice(Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
