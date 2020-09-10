from django.urls import path, re_path
from .views import index,rest_feed_detail, rest_feeds, rest_items

urlpatterns = [
    path('', index, name='index'),
    path('feeds/', rest_feeds, name='rest-feeds'),
    re_path(r'^feed/(?P<pk>[0-9]+)/$', rest_feed_detail, name='rest-feeds-detail'),
    path('items/', rest_items, name='rest-items')

]