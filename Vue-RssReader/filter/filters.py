from django_filters import FilterSet, ChoiceFilter
from .models import Person


class PersonFilter(FilterSet):

    # 필터 기능을 할 목록 파라미터
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending'),
    )
    ordering = ChoiceFilter(label='Ordering', choices = CHOICES, method='filter_by_order')

    class Meta:
        model = Person
        # Person 테이블 중 필터기능 추가 목록들
        fields = {
            'first_name' : ['icontains'],
            'last_name' : ['icontains'],
        }


    def filter_by_order(self, queryset, name, value):
        expression = 'first_name'  if value == 'ascending' else '-first_name'
        return queryset.order_by(expression)




class PersonFilter_(FilterSet):
    class Meta:
        model = Person
        fields = {
        "first_name": ["exact", "contains"],
        "last_name": ["exact"]
        }
