from django.urls import path
from . import views

# app_name = 'questions'
# urlpatterns = [
#     #path('admin/', admin.site.urls),# 어드민이라는 url이 들어오면 여기로 연결해라
#     path('',views.index, name='index'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('<int:question_id>/', views.detail, name='question_detail'),
# ]
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'), 
    path('<int:question_id>/result/', views.result, name='result'), 
]