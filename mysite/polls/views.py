from django.http import HttpResponse

def index(requset):
    return HttpResponse("Hello, world.")

def some_url(requset):
    return HttpResponse("some url를 구현해 봤습니다.")