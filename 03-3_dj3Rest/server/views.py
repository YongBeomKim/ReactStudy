from django.shortcuts import render
from django.http import JsonResponse


def api(request):
    data = {
        "items": [
            {"id": 1, "name": "Apples", "price": "$2"},
            {"id": 2, "name": "Peaches", "price": "$5"},
        ]
    }
    return JsonResponse(data, status=200)


def index(request):
    r"""Adding the React.js's Contents
    :: props :: django to React.js props
    :: js_app_name :: webpack bundle js"""

    props = {
        "name": "Python Django",
        "more": "momukji lab",
    }
    js_app_name = "index.bundle.js"

    markdown = (
        "### <small>example of</small> **DJANGO3 for APIs**\n"
        + "- [Github](https://github.com/wsvincent/djangoforapis_30)\n"
        + "```python\n"
        + "@register.filter()\n"
        + "@stringfilter\n"
        + "def markdown(value):\n"
        + "    return md.markdown(\n"
        + '        value, extensions=["markdown.extensions.fenced_code"]\n'
        + ")\n"
        + "```\n"
    )

    content = {
        "props": props,
        "js_app_name": js_app_name,
        "content": markdown,
    }
    return render(request, "index.html", content)
