from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    # Django 에서 CRUD 메서드를 Vue.js 인스턴스로 대체
    path('', TemplateView.as_view(template_name='crud/index.html')),
]