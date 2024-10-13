from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET']) # question_list가 get 요청을 처리할 것이다 라는 의미
def question_list(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many = True) # many = True 시니얼라이저에서 여러개의 옵션을 주기위한 소스
    return Response(serializer.data)