from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import  User
from .filters import UserFilter

def search(request):
    # view 함수에 사용할 데이터를 호출
    user_list = User.objects.all()

    # filter 의  Query Set 캐시를 활성화 한다.
    user_filter = UserFilter(request.GET, queryset=user_list)
    content = {'filter': user_filter}
    return render(request, 'search/user_list.html', content)