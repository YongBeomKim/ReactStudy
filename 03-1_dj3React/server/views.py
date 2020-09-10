from django.shortcuts import render
from .utils import render_to_react


def index(request):
    return render(request, "index.html")


def react(request):

    r"""Django Content to webpack React
    """

    props = {
        "name": "Python Django",
        "more": "momukji lab",
    }

    js_app_name = "index.bundle.js"
    template_name = "react.html"

    return render_to_react(
        request, template=template_name, js_app_name=js_app_name, props=props
    )
