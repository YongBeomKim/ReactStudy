from django.shortcuts import render
from .utils import render_to_react


# def index(request):
#     return render(request, "index.html")


# Render to Django HTML & React.js JSX

def index(request):

    props = {
        "name": "pato",
        "more": "Ken"
    }

    template_name = "index-jsx.html"
    js_app_name = "index.bundle.js"

    return render_to_react(
        request,
        template=template_name,
        js_app_name=js_app_name,
        props=props
    )
