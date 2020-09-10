from django.shortcuts import render
from .models import Person,People

from django_tables2 import SingleTableView, SingleTableMixin
from .userfunc import PeopleTable, PeopleFilter


from django_filters.views import FilterView

class PeopleFilterView(SingleTableMixin, FilterView):
    model = People
    table_class = PeopleTable
    filterset_class = PeopleFilter
    template_name = "excel/template.html"

    def get_queryset(self):
        return super(PeopleFilterView, self).get_queryset().select_related("first_name")

    def get_table_kwargs(self):
        return {"template_name": "django_tables2/bootstrap.html"}








# ex0-1) SingleTableView
# django-table2 의 제너릭뷰 사용1
class PersonList(SingleTableView):
    model = People
    template_name = 'excel/person.html'
    table_pagination = False

# ex0-2) SingleTableMixin
# django-table2 의 제너릭뷰 사용2
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


# ex1) DB의 Query Set
def people_one(request):
    content = Person.objects.all()
    print("\ntype : {}\ndata : {}\n".format(
        type(content), content))
    # type <class 'django.db.models.query.QuerySet'>
    # data <QuerySet [<Person: Person object (1)>, <Person: Person object (2)>]>
    return render(request, 'excel/people.html', {'people': Person.objects.all()})


# ex2) List to dict 의 활용
from django_tables2 import RequestConfig
from .userfunc import NameTable

def people(request):
    data = [{'name': 'Bradley', 'age': 12, 'sex':'female'},
            {'name': 'Stevie',  'age': 21, 'sex':'male'},]
    table = NameTable(data)
    # .RequestConfig() 메소드는
    # request.GET 데이터를 호출하고, 결과를 Ajax 출력
    RequestConfig(request).configure(table)
    return render(request, 'excel/people2.html', {'table': table})


# ex3) DataFrame 에서 컬럼만 추출하여 모델을 생성하고
# https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
# 생성된 인스턴스로 객체를 출력한다. 컬럼별 관리를 요하므로 우선은 이걸로 진행
# https://github.com/jieter/django-tables2/issues/288

# 필터 인스턴스 정의하기
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .userfunc import SimpleTable, SimpleFilter

class SimpleFilteredView(SingleTableMixin, FilterView):
    table_class = SimpleTable
    filterset_class = SimpleFilter
    template_name = "bootstrap_template.html"

    # redirect 작업을 진행
    def get_queryset(self):
        return super(SimpleFilteredView, self).get_queryset().select_related("name")

    def get_table_kwargs(self):
        return {"template_name": "django_tables2/bootstrap.html"}


from .userfunc import SimpleCountryTable
def pandas_table(request):

    ndf = pd.DataFrame([
        {'name': 'china',
         'population': 12,
         'tz': 'Asia/Shanghai',
         'visits': 82,
         'summary': 'nice place',
         '기타': '서울시'},

        {'name': 'usa',
         'population': 1,
         'tz': 'whatever',
         'visits': 25,
         'summary': 'good place',
         '기타': '수원시'},

        {'name': 'japan',
         'population': 120,
         'tz': 'Asia/Seoul',
         'visits': 32,
         'summary': 'poor place',
         '기타':'부산시'},

        {'name': 'usa',
         'population': 80,
         'tz': 'USA/NewYork',
         'visits': 12,
         'summary': 'nice place',
         '기타':'어쩌고'},
    ])

    ndf   = ndf.to_dict(orient = 'records')
    table = SimpleCountryTable(ndf, orderable=True)

    # paginate={'per_page': 2} : 페이지별 출력할 index
    # RequestConfig(request, paginate=False).configure(table)
    RequestConfig(request, paginate={'per_page': 2}).configure(table)


    # 출력 쿼리 조건만 맞추면 해당 포맷으로 출력한다
    # http://localhost:8000/excel/pandas/?_export=csv
    # http://localhost:8000/excel/pandas/?_export=xls
    # http://localhost:8000/excel/pandas/?_export=xlsx
    # http://localhost:8000/excel/pandas/?_export=json

    # ! pip install tablib
    # Get 쿼리문으로 csv 파일을 다운로드

    # table 객체를 csv, xls, json등 외부출력 링크를 생성한다
    # 외부로 출력하는 Query를 생성한다
    from django_tables2.export.export import TableExport

    # 각 타입별 출력이 가능한 함수
    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table,
                               # 이미지등 출력에 불필요한 컬럼은 제외
                               exclude_columns=('name', '참고자료'))
        # 출력을 위한 카드이름을 지정 가능하다
        return exporter.response('MuyongCard.{}'.format(export_format))
    return render(request, "excel/people3.html", {"table": table})








# https://django-tables2.readthedocs.io/en/latest/pages/filtering.html
from django_tables2 import SingleTableView
from django_filters.views import FilterView
class SimpleCountryFilter(SingleTableView, FilterView):
    table_class = SimpleCountryTable
    template_name = 'excel/filter.html'
    # filterset_class = PersonFilter





# ex4) pandas를 보다 짧게 구현해보자, 그런데 동작안함
# https://stackoverflow.com/questions/44123575/how-to-display-rows-of-csv-file-in-django
from django_tables2.tables import Table
import pandas as pd

def table(request):
    # data = pd.DataFrame({"A": [1, 2, 3, 4],
    #                    "B": [10, 20, 30, 40],
    #                    "C": [100, 200, 300, 400]})

    data = [{'name': 'Bradley', 'age': 12, 'sex':'female'},
            {'name': 'Stevie',  'age': 21, 'sex':'male'},]
    # table = Table(data.to_dict())
    # table = Table(data.to_dict(orient='list'))
    # table = Table(data.to_dict(orient='records'))
    table = Table(data, orderable=True)
    RequestConfig(request, paginate=True).configure(table)
    content  = {'table': table}
    return render(request, "excel/table.html", content)





# Create your views here.
from .userfunc import check_xls

# https://stackoverflow.com/questions/39003732/display-django-pandas-dataframe-in-a-django-template
# 원래는 파일이 Post 로 넘어오면 처리내용을 출력
def index(request):

    if "GET" == request.method: # 바로 페이지 호출시
        return render(request, 'excel/index.html', {})


    else:  # form 에서 파일이 넘어왔을 때
        # 참고로 app/table url경로로 자동 넘어간다!! (오호라!!)
        excel_file = request.FILES["excel_file"]
        df_table, name  = check_xls(excel_file)
        request.FILES["excel_file"] = False # excel_file 초기화
        # df_table.to_csv('media/excel/result.csv', index=None)
        # df_table = df_table.iloc[7:15, 8:17]
        df_html  = df_table.to_html(classes="striped", index=None)
        content  = {
            "excel_type" : name,
            "excel_html" : df_html,
        }
        return render(request, 'excel/index.html', content)






# csv : https://gist.github.com/jonperron/733c3ead188f72f0a8a6f39e3d89295d
# xls : https://stackoverflow.com/questions/35267585/django-pandas-to-http-response-download-file
from io import BytesIO

def output_xls(request):
    # 출력하고 싶은 Pandas 결과물
    if df_table == False:
        return None

    # 메모리에 있는 DataFrame을
    # 버퍼에서 엑셀파일을 생성하고 여기에 덮어씌운다
    excel_file = BytesIO()
    xlwriter   = pd.ExcelWriter(excel_file, engine='xlsxwriter')

    # 메모리에 저장된 데이터 프레임을 엑셀파일로 저장
    df_table.to_excel(xlwriter, 'sheetname')
    xlwriter.save()
    xlwriter.close()

    # 버퍼값이 0이 될때 까지 반복해서, Excel파일 메모리로 불러온다 (중요!)
    excel_file.seek(0)
    type_name = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    # MIME Type 으로 브라우저가 인식가능한 포맷으로 변환
    response = HttpResponse(excel_file.read(), content_type=type_name)
    # Content-Disposition 헤더값으로 파일이름을 구체적으로 지정한다
    response['Content-Disposition'] = 'attachment; filename=muyong_report.xlsx'
    return response



import logging

# logger 객체를 호출합니다
logger = logging.getLogger('mylogger')

def my_view(request, arg1, arg):
    # 필요한 로직
    if bad_mojo:
        # Error 레벨의 레코드를 작성합니다
        logger.error('Somthing went wrong!')