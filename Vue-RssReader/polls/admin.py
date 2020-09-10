from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# StackedInline 은 기본값으로,
# TabularInline 는 inlines 에 포함시
# 보다 조밀하고 테이블 기반 형식으로 표시된다
# https://docs.djangoproject.com/ko/2.1/intro/tutorial07/

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # 필드의 나열순서를 정의한다
    list_display  = ('question_text', 'pub_date')

    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question Statement',
            {'fields': ['question_text']}),
        ('Date Information',
            {'fields': ['pub_date'],
             'classes': ['collapse']})
    ]
    # ChoiceInline 모델을 함께 표시
    inlines       = [ChoiceInline]
    # 사이드에 필터객체 표시
    list_filter   = ['pub_date']
    # 검색필터 활성화 (검색대상)
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)