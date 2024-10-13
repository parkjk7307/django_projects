from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
# Create your models here.
# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션이라는걸 만든다.
# 이 모델에 맞는 테이블을 만듭니다.
# 질문: 여름에 놀러간다면 어디에 갈래?
# 산
# 강
# 바다
# 도심 호캉스

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='질문')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일') # auto_now_add 퀘스찬이 처음 생길때 시간을 add한다.
    # 모델의 변경사항
    # is_something = models.BooleanField(default=False)
    # average_score = models.FloatField(default=0.0)
    # score = models.FloatField(default=0)
    # is_something_wrong = models.BooleanField(default=False)
    # json_field = models.JSONField(default=dict)
    @admin.display(boolean=True, description='최근생성(하루기준)')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        if self.was_published_recently():
            new_badge = 'NEW!!!'
        else:
            new_badge = ''
        return f'{new_badge} 제목: {self.question_text}, 날짜: {self.pub_date}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # 모델 생성 완료
    

    def __str__(self):
        return f'[{self.question.question_text}] / {self.choice_text}'
