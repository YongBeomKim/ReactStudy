from django.urls import re_path, path
from .views import index, output_xls, table, people, people_one, PeopleFilterView, pandas_table, PersonList
app_name="excel"

urlpatterns = [
    path('', index, name='index'),
    #path('table/', table, name='index'),
    path('down/', output_xls, name='down'),
    path('people/', people, name="people"),
    path('peopledb/', people_one, name="people"),
    path('person/', PersonList.as_view(), name='person'),
    path('pandas/', pandas_table, name='pandas'),
    # path("filter/", SimpleFilteredView.as_view(), name="filter"),
    path("filter/", PeopleFilterView.as_view(), name="filter"),
]
