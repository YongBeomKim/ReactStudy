from crud.views import ArticleViewSet
from rest_framework import routers

# 라우터 기능(Rest api 의 Url 매핑) 을 활성화
# urls.py 활용을 위해 server 폴더에 적용
router = routers.DefaultRouter()

# crud App의 Mapping 경로 : /article
router.register(r'article', ArticleViewSet)