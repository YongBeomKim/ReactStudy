from django.shortcuts import render
from server.utils import render_to_react
from django.db.models import Q
from .models import Journal, Category

# Create your views here.

# param's boolean validation check
# `None` is Change to `False`
def valid_string(param):
    # Exception Values
    if param in [None, "", "Choose...", "0", "1000?"]:
        return False
    else:
        return param


def valid_query(param):
    return param != "" and param is not None


def BootstrapFilterView(request):

    r"""Multi Parametor Filtering Function
    """

    # Title filter functions
    title_contains_query = valid_string(request.GET.get("title_contains"))
    id_exact_query = valid_string(request.GET.get("id_exact"))
    title_or_author_query = valid_string(request.GET.get("title_or_author"))
    category = valid_string(request.GET.get("category"))

    # `String` Parametor Filtering
    querySet = Journal.objects.filter(
        Q(title__icontains=title_contains_query)
        | Q(id=id_exact_query)
        | Q(title__icontains=title_or_author_query)
        | Q(author__name__icontains=title_or_author_query)
        | Q(categories__name=category)
    )

    # `Except String` Parametor Filtering
    # Count filter functions
    view_count_min = request.GET.get("view_count_min")
    view_count_max = request.GET.get("view_count_max")
    if valid_query(view_count_min):
        querySet = querySet.filter(views__gte=view_count_min)
    elif valid_query(view_count_max):
        querySet = querySet.filter(views__lt=view_count_max)

    # DateTime filter functions
    date_min = request.GET.get("date_min")
    date_max = request.GET.get("date_max")
    if valid_query(date_min):
        querySet = querySet.filter(publish_date__gte=date_min)
    elif valid_query(date_max):
        querySet = querySet.filter(publish_date__lt=date_max)

    # Review check box filter functions
    reviewed = request.GET.get("reviewed")
    notReviewed = request.GET.get("notReviewed")
    if reviewed == "on":
        querySet = querySet.filter(reviewed=True)
    elif notReviewed == "on":
        querySet = querySet.filter(reviewed=False)

    # result validation check : None & length is Zero.
    if querySet != None:
        if len(querySet) == 0:
            querySet = None

    categories = Category.objects.all()
    content = {"queryset": querySet, "categories": categories}
    return render(request, "core/bootstrap.html", content)
