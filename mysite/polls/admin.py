from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Create_Date', {'fields': ['pub_date'], 'classes': ['collapse']}),        
    ]
    readonly_fields = ['pub_date'] # model.py에 적혀있는 에러 해결법 auto_now_add=True
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)