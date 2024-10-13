from django.urls import path
from .views import *


urlpatterns = [
    # path('', question_list, name='default-view'),  # 기본 경로 처리 추가
    # path('question/', question_list, name='question-list'),
    # path('question/<int:id>/', question_detail, name='question-detail'),
    path('question/', QuestionList.as_view(), name='question-list'),
    path('question/<int:id>/', QuestionDetail.as_view(), name='question-detail'),
]