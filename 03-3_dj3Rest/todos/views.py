from django.shortcuts import render

from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def index(request):
    r"""Adding the React.js's Contents
    :: props :: django to React.js props
    :: js_app_name :: webpack bundle js"""

    props = [
        {"id": 1, "title": "1st Todo", "body": "Learn Django properly."},
        {"id": 2, "title": "Second item", "body": "Learn Python"},
        {"id": 3, "title": "Learn HTTP", "body": "It's Important."},
    ]
    js_app_name = "todo.bundle.js"

    markdown = (
        "```python\n"
        + "def markdown(value):\n"
        + "    return md.markdown(\n"
        + ")\n"
        + "```\n"
    )

    content = {
        "props": props,
        "js_app_name": js_app_name,
        # "content": markdown,
    }
    return render(request, "todos/index.html", content)
