from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
import requests


register = template.Library()


@register.simple_tag
def build(app_name):
    r"""Connecting with the WebPackDev or Django Static

    * First, checking the dev server & using it

    * if status code is not 200, then using bundle file
    """

    url_link = f"http://localhost:3000/{app_name}"
    file_name = f"dist/{app_name}"
    try:
        if requests.get(url_link).status_code == 200:
            return url_link
    except:
        return static(file_name)
