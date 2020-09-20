from django.shortcuts import render


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
        "```python\n"
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
