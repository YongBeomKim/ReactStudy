from django.shortcuts import render


# render to React Template
def render_to_react(request, template=str, js_app_name=str, props=dict):
    r"""Django data Rendering to the React.js Props

    * template : django Template name

    * jsx_app_name : React.js build / HRM file name

    * props : django date to React.js
    """

    content = {
        "js_app_name": js_app_name, "props": props}

    return render(
        request, template, content
    )
