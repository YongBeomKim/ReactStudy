from django.shortcuts import render
# Create your views here.


# 별도의 파일이름을 추가하지 않기 위해 사용했을 뿐
# 실질적으로 views.py 기능을 하고 있지는 않다
# 단지 serializers(직렬화기) 와 models.py를 연결하는 역활을 하고 있다
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset         = Article.objects.all()
    serializer_class = ArticleSerializer
