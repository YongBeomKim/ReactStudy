from django import template
from django.conf.urls.static import static
import requests


register = template.Library()


@register.simple_tag
def react(app_name, port=3000):

    r"""Connecting with the WebPackDev or Django Static

    * First, checking the dev server & using it

    * if status code is not 200, then using bundle file
    """

    # When webpack dev server port is 3000 ...
    dev_server_link = f"http://localhost:{port}/{app_name}"
    # Build file name & location ....
    file_name = f"dist/{app_name}"

    try:
        # First Checking dev server & link local bundle file
        if requests.get(dev_server_link).status_code == 200:
            return dev_server_link
        else:
            return static(file_name)

    except:
        return static(file_name)
