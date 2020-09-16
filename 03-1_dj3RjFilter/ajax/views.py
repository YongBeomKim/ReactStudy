from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.

from time import time
import json
from django.http import JsonResponse

# ajax data
data = {
    "items": [
        {"id": 1, "name": "Apples", "price": "$2"},
        {"id": 2, "name": "Peaches", "price": "$5"},
    ]
}

# request.is_ajax() is Deseperated in Djang 3.1
# https://docs.djangoproject.com/en/3.1/releases/3.1/#id2
class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get("button_text")

        if request.is_ajax():
            # if request.headers.get("x-requested-with") == "XMLHttpRequest":
            content = {"seconds": time()}
            return JsonResponse(content, status=200)
        return render(request, "ajax/index.html")

    def post(self, request):
        card_text = request.POST.get("text")
        resultText = f"I have got : {card_text}"
        content = {
            "data": resultText,
        }
        return JsonResponse(content, status=200)


from .utils import render_to_react


def reactApi(request):
    content = {"data": data}
    return JsonResponse(content, status=200)


def reactAjax(request):
    props = {
        "name": "Python Django",
        "more": "momukji lab",
    }
    return render_to_react(
        request, template="ajax/react.html", js_app_name="index.bundle.js", props=props
    )


# GET Transition
# def reactAjax(request):
#
# if request.is_ajax():
# content = {"data": data}
# return JsonResponse(content, status=200)
#
# else:
# props = {
# "name": "Python Django",
# "more": "momukji lab",
# }
#
# js_app_name = "index.bundle.js"
# template_name = "ajax/react.html"
#
# return render_to_react(
# # request, template=template_name, js_app_name=js_app_name, props=props
# )
#


# def ajax(request):
#     data = {
#         "Organization": [
#             {"name": "Sangmin Park", "github": "steadily-worked"},
#             {"name": "Woosik Kim", "github": "well-balanced"},
#             {"name": "Hyeonsu Lee", "github": "incleaf"},
#             {"name": "Hoseon Lee", "github": "indante"},
#         ]
#     }
#     response = json.dumps(data)
#     return HttpResponse(response)


# # merge Single Function
# def main(request):
#     data = {
#         "Organization": [
#             {"name": "Sangmin Park", "github": "steadily-worked"},
#             {"name": "Woosik Kim", "github": "well-balanced"},
#             {"name": "Hyeonsu Lee", "github": "incleaf"},
#             {"name": "Hoseon Lee", "github": "indante"},
#         ]
#     }
#     content = {"data": json.dumps(data)}
#     return render(request, "ajax/index.html", content)

