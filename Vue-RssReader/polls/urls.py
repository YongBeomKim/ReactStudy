from django.urls import re_path, path
from .views import index, detail, results, vote, plot_bokeh

app_name="polls"
urlpatterns = [
    path('',                           index,   name="index"),
    path('<int:question_id>/',         detail,  name='detail'),
    path('<int:question_id>/results/', results, name="results"),
    path('<int:question_id>/vote/',    vote,    name='vote'),
    path('bokeh/',                  plot_bokeh, name="bokeh")
]