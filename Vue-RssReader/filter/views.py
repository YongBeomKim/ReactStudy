from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Person
from .filters import PersonFilter
from .forms import ContactForm, SnippetForm

# Django 에서 from 객체의 처리내용 알아보자
def content(request):
    if request.method == 'POST':
        # forms.py 에서 form 관리할 필드를 정의
        # template 에서는 {{form}} 만 입력
        form = ContactForm(request.POST)
        if form.is_valid():
            # 유효성 검사 후 처리할 내용을 추가
            name  = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)


    # forms.py 에서 설정한 내용을 Template에서 자동으로 구현
    else:
        form = ContactForm()
    content = {'form':form}
    return render(request, 'filter/form.html', content)


# Form 처리된 내용을 DataBase와 연결
def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            print("form valid complete")
            form.save()  # 유효성 검사 후 DataBase 저장 (참 쉽죠?)


    # forms.py 에서 설정한 내용을 Template에서 자동으로 구현
    form = SnippetForm()
    content = {'form':form}
    return render(request, 'filter/form.html', content)



class PersonListView(ListView):
    model = Person
    # context_object_name = Generic View 객체명을 지정가능
    template_name = 'filter/person_list.html'

    # 제너릭 뷰가 개별 튜플의 pk를 호출하지 않음을 보완하는 사용자 함수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PersonFilter(self.request.GET, queryset=self.get_queryset())
        return context



class PersonDetailView(DetailView):
    model = Person
    template_name = 'filter/person_detail.html'


# from django.shortcuts import render
#
# # Create your views here.
# from django.http import HttpResponse
# from django_filters.views import FilterView
# from django_tables2 import RequestConfig, SingleTableMixin
#
# from django.views.generic import ListView, DetailView
# from .models import Person
#
# class SnippetListView(ListView):
#     model = Person
#     template_name = 'filter/snippet_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = SnippetListView(self.request.GET, queryset=self.get_queryset())
#         return context
#
#
#
# class SnippetDetailView(DetailView):
#     model = Person
#     template_name = 'filter/snippet_detail.html'
#
#
#
# def index(request):
#     return HttpResponse("django-table2 django-filter django-crisy-form 사용하기")
#
# from .tables import PersonTable
# from .filters import PersonFilter
# from .models import Person
#
# class FilteredPersonListView(SingleTableMixin, FilterView):
#     table_class = PersonTable # 테이블 인스턴스
#     model = Person
#     template_name = "filter/template.html"
#
#     # 필터 조건함수
#     filterset_class = PersonFilter
#
#     def get_queryset(self):
#         return super(FilteredPersonListView, self).get_queryset()
#         # return super(FilteredPersonListView, self).get_queryset().select_related("first_name")
#
#     def get_table_kwargs(self):
#         return {"template_name": "django_tables2/bootstrap.html"}
#
#
# from .filters import PersonFilterRaw
#
# def people_list(request):
#     filter = PersonFilterRaw(request.GET, queryset=Person.objects.all())
#     return render(request, 'filter/filter.html', {'filter': filter})
