from django.shortcuts import render
from django.http import JsonResponse
from .utils import render_to_react
import json


def api(request):
    data = {
        "items": [
            {"id": 1, "name": "Apples", "price": "$2"},
            {"id": 2, "name": "Peaches", "price": "$5"},
        ]
    }
    return JsonResponse(data, status=200)


# React.js 는 단방향 Binding 만 되므로,
# 양방향의 Ajax 를 활용하는 방법은 적용 가능하지 않는 것으로 생각....
# Form 데이터를 Props 로 전달하는 방식으로 활용하기...
def index(request):
    # Django 3.1
    # https://docs.djangoproject.com/en/3.1/releases/3.1/#id2
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        jsonData = {
            "items": [
                {"id": 1, "name": "Apples", "price": "$2"},
                {"id": 2, "name": "Peaches", "price": "$5"},
            ]
        }
        # JsonResponse : {dict} to Json
        return JsonResponse(jsonData, status=200)

    props = {
        "name": "Python Django",
        "more": "momukji lab",
    }

    return render_to_react(
        request, template="index.html", js_app_name="index.bundle.js", props=props
    )
