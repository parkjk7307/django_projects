from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

# @api_view(['GET','POST']) # question_list가 get 요청을 처리할 것이다 라는 의미
# def question_list(request):
#     if request.method == 'GET':
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def question_detail(request, id):
#     question = get_object_or_404(Question, pk=id)
    
#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:    
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class QuestionList(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(APIView):
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        question = get_object_or_404(Question, pk=id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)