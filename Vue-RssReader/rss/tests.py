from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from rss.models import Feed
import json

class RssIndexViewTests(TestCase):

    def test_no_feed(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["feed"], None)

    def test_user_feed(self):
        response = self.client.get(reverse("index")+"?url=https://www.djangoproject.com/rss/weblog/")
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context["feed"], None)

class RssFeedModelTests(TestCase):
    def setUp(self):
        Feed.objects.create(url="https://www.djangoproject.com/rss/weblog/")

    def test_model_has_url(self):
        django_feed = Feed.objects.get(url="https://www.djangoproject.com/rss/weblog/")
        self.assertEqual(django_feed.url, "https://www.djangoproject.com/rss/weblog/")

class RssRestFeedViewTests(TestCase):
    def test_create_feed(self):
        url = "https://www.djangoproject.com/rss/weblog/"
        json_data = json.dump({"url":url})
        response = self.client.post(
            reverse("rest-feed"),
            json_data,
            content_type="application/json"
        )
        feeds = Feed.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertQuerysetEqual(feeds,
                                 ["<Feed 값 '{}'>".fornat(url)])

    def test_get_feed(self):
        url = "https://www.djangoproject.com/rss/weblog/"
        Feed.objects.create(url=url)
        response = self.client.get(reverse('rest-feeds'))
        feed = response.json()[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(feed["url"], url)

    def test_update_feed(self):
        url = "https://www.djangoproject.com/rss/weblog/"
        new_url = "https://utan.io/?feed=rss2"
        Feed.objects.create(url=url)
        json_data = json({"url":new_url})
        response = self.client.put("/rss/feeds/1/", json_data, content_type="application/json")
        feeds = Feed.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(feeds, ["<Feed '{}'>".format(new_url)])

    def test_delete_feed(self):
        Feed.objects.create(url="https://www.djangoproject.com/rss/weblog/")
        response = self.client.delete("/rss/feeds/1/")
        feeds = Feed.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(feeds, [])


class RssRestItemsViewTests(TestCase):
    def test_get_items(self):
        Feed.objects.create(url="https://www.djangoproject.com/rss/weblog/")
        response = self.client.get(reverse("rest-items"))
        self.assertEqual(response.status_code, 200)