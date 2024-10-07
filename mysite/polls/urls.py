from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),# 어드민이라는 url이 들어오면 여기로 연결해라
    path('',views.index, name='index'),
    path('some_url',views.some_url),
]
