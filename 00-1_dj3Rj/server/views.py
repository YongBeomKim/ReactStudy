from django.shortcuts import render
from django.http import JsonResponse
from .utils import render_to_react


def api(request):
    data = {
        "items": [
            {"id": 1, "name": "Apples", "price": "$2"},
            {"id": 2, "name": "Peaches", "price": "$5"},
        ]
    }
    return JsonResponse(data, status=200)


def index(request):

    r"""Django Content to webpack React
    """

    props = {
        "name": "Python Django",
        "more": "momukji lab",
    }

    js_app_name = "index.bundle.js"
    template_name = "index.html"

    return render_to_react(
        request, template=template_name, js_app_name=js_app_name, props=props
    )
