from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Document(models.Model):
    description = models.CharField(blank=True, max_length=225)
    document = models.FileField(upload_to='uploaded-documents/')

    class Meta:
        permissions = [('can_view_documentss', 'Can clean documentss')]


class User(AbstractUser):
    pass

