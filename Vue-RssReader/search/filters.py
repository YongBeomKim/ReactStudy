from django.contrib.auth.models import User,Group
from django_filters import FilterSet, CharFilter, NumberFilter, ModelMultipleChoiceFilter
from django import forms

# auth 저장된 사용자 정보를 필터링
class UserFilter_(FilterSet):

    # filter 에 사용할 QuerySet 연결내용
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserFilter_(FilterSet):
    # 특정한 컬럼은 포함여부를 조건으로 검색한다
    first_name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserFilter_(FilterSet):
    first_name  = CharFilter(lookup_expr = 'icontains')
    date_joined = NumberFilter(lookup_expr='year')

    # 필터링 결과 출력할 필드들
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class UserFilter(FilterSet):

    first_name      = CharFilter(lookup_expr='icontains')
    year_joined     = NumberFilter(name='date_joined', lookup_expr='year')
    year_joined__gt = NumberFilter(name='date_joined', lookup_expr='year__gt')
    year_joined__lt = NumberFilter(name='date_joined', lookup_expr='year__lt')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


# ___ new form style ___________________________


class UserFilter(FilterSet):
    first_name = CharFilter(lookup_expr='icontains')
    year_joined = NumberFilter(name='date_joined', lookup_expr='year')
    groups = ModelMultipleChoiceFilter(
        queryset = Group.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'year_joined', 'groups',]


