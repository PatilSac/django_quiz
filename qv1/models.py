from django.db import models


# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=50, null=True)
    date = models.DateField(auto_now=True)
    url = models.URLField(verbose_name='URL', null=True)


class Question(models.Model):
    questions = models.CharField(max_length=100)
    choise1 = models.CharField(max_length=50, null=False)
    choise2 = models.CharField(max_length=50, null=False)
    choise3 = models.CharField(max_length=50, null=False)
    choise4 = models.CharField(max_length=50, null=False)
    answer = models.CharField(max_length=50, null=False)
