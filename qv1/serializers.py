from rest_framework.serializers import ModelSerializer
from .models import Question, Quiz


class Quizserilizer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class Questionserilizer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
