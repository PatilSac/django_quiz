from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET','POST'])
def index (request):
    if request.method == 'GET':
        return Response(data={'message':'This is test reponse for GET request'}, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        return Response(data=request.data,  status=status.HTTP_200_OK)
    
    else:
        return Response(data = {'message':'Wrong request'})


class Message(APIView):
    
    def get(self, request):
        return Response(data="This is GET methode from class based view",status=status.HTTP_200_OK)


    def post(self, request):
        return Response(data="This is post method from class based view"+str(request.data),status=status.HTTP_200_OK)
