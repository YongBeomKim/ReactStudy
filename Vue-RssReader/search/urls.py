from django.urls import path
from .views import search
from django_filters.views import FilterView
from .filters import UserFilter


app_name = 'search'
urlpatterns = [
    # path('', search, name='index'),
    path('', FilterView.as_view(filterset_class = UserFilter,
                                template_name = 'search/user_list.html'),
         name='index'),

]


