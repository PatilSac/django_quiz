from django.urls import path
from .views import Quizez

urlpatterns = [

    path ('quizes/', Quizez.as_view(), name='quizez')
]