# from django.shortcuts import render
# from rest_framework.views import APIView
# from .models import Question, Quiz
# from .serializers import Questionserilizer, Quizserilizer
# from rest_framework import status
# from rest_framework.response import Response
# from django.http import Http404
#
#
# # Create your views here.
# class Quizez(APIView):
#
#     def get_object(self):
#         try:
#             return Quiz.objects.all()
#         except:
#             raise Http404
#
#     def get(self, request):
#         q = self.get_object()
#         serilizer = Quizserilizer(q, many=True)
#         return Response(data=serilizer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serilizer = Quizserilizer(data=request.data)
#         try:
#             if serilizer.is_valid():
#                 serilizer.save()
#                 return Response(serilizer.data, status=status.HTTP_201_CREATED)
#
#         except Exception as e:
#             print(e)
#             return Response(serilizer.errors, status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request):
#         q = Quiz.objects.get(id=request.data['id'])
#         q.delete()
#         return Response(data='Delete', status=status.HTTP_410_GONE)
#
#     def put(self, request):
#         q = Quiz.objects.get(id=request.data['id'])
#         serilizer = Quizserilizer(q, data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(data=serilizer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serilizer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


from rest_framework import generics
from .models import Quiz
from .serializers import Quizserilizer


class Quizez(generics.ListCreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = Quizserilizer


