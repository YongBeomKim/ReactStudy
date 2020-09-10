from django.shortcuts import render
from server.utils import render_to_react
from django.db.models import Q
from .models import Journal, Category

# Create your views here.

# param's boolean validation check
def is_valid_queryparam(param):
    # if param is None:
    return param != "" and param is not None


def BootstrapFilterView(request):
    # qs = Journal.objects.all()

    # Title filter functions
    title_contains_query = request.GET.get("title_contains")
    id_exact_query = request.GET.get("id_exact")
    title_or_author_query = request.GET.get("title_or_author")

    if is_valid_queryparam(title_contains_query):
        qs = Journal.objects.all().filter(title__icontains=title_contains_query)
        content = {"queryset": qs}

    elif is_valid_queryparam(id_exact_query):
        qs = Journal.objects.all().filter(id=id_exact_query)
        content = {"queryset": qs}

    elif is_valid_queryparam(title_or_author_query):
        qs = (
            Journal.objects.all()
            .filter(
                Q(title__icontains=title_or_author_query)
                | Q(author__name__icontains=title_or_author_query)
            )
            .distinct()
        )

    # Count filter functions
    view_count_min = request.GET.get("view_count_min")
    view_count_max = request.GET.get("view_count_max")

    if is_valid_queryparam(view_count_min):
        # Grater Than Equal to ...
        qs = Journal.objects.all().filter(views__gte=view_count_min)

    elif is_valid_queryparam(view_count_max):
        # Less Than .. (Except Equal condition)
        qs = Journal.objects.all().filter(views__lt=view_count_max)

    # DateTime Filter
    date_min = request.GET.get("date_min")
    date_max = request.GET.get("date_max")

    if is_valid_queryparam(date_min):
        qs = Journal.objects.all().filter(publish_date__gte=date_min)

    elif is_valid_queryparam(date_max):
        qs = Journal.objects.all().filter(publish_date__lt=date_max)

    # Category & Review Filter
    category = request.GET.get("category")
    reviewed = request.GET.get("reviewed")
    notReviewed = request.GET.get("notReviewed")
    categories = Category.objects.all()

    if is_valid_queryparam(category) and category != "Choose...":
        qs = Journal.objects.all().filter(categories__name=category)

    if reviewed == "on":
        qs = Journal.objects.all().filter(reviewed=True)

    elif notReviewed == "on":
        qs = Journal.objects.all().filter(reviewed=False)

    content = {"queryset": qs, "categories": categories}
    return render(request, "core/bootstrap.html", content)
