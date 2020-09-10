from django_filters import FilterSet
from .models import Person, People

# 필터 관리용 인스턴스
class PeopleFilter(FilterSet):
    class Meta:
        model = People
        fields = {
        "first_name": ["exact", "contains"],
        "last_name": ["exact"]
        }


# 테이블 데이터 인스턴스
import django_tables2 as tables

class PeopleTable(tables.Table):
    first_name = tables.Column(linkify=True)
    last_name  = tables.Column(linkify=True)
    class Meta:
        model = People
        template_name = "django_tables2/bootstrap.html"



# ex1) django_table2 에서 제공하는 bootstrap 템플릿 활용
class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap.html'

# ex2) tables 함수 활용
# dict 타입으로 사용시에는 컬럼마다 선언을 해 줘야 한다
class NameTable(tables.Table):
    name = tables.Column()
    age  = tables.Column()
    sex  = tables.Column()



# ex3) DataFrame 자료활용
# 일단 end-point를 명확히 해자
# 추후 컬럼추출 방식을 개선해보자
# https://github.com/jieter/django-tables2/pull/295/commits/590f6857734bb23316adffa941fdf339f4154fcb

# 컬럼의 합계 계산하는 함수
class SummingColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return sum(bound_column.accessor.resolve(row) for row in table.data)




from django_filters import FilterSet

class SimpleFilter(FilterSet):

    class Meta:
        fields = {
            "name":   ["exact", "contains"],
            "visits": ["exact"]}


class SimpleTable(tables.Table):

    tz         = tables.Column(verbose_name='time zone')
    name       = tables.Column(footer='합계:')
    population = SummingColumn()
    visits     = tables.Column()
    summary    = tables.Column(order_by=("name", "population"))

    class Meta:
        template_name = "django_tables2/bootstrap.html"





class SimpleCountryTable(tables.Table):
    import itertools
    ATTRIBUTES = {
        'th': {
            '_ordering': {
                'orderable': 'sortable',  # Instead of `orderable`
                'ascending': 'ascend',  # Instead of `asc`
                'descending': 'descend'  # Instead of `desc`
            }
        }
    }

    # .objects.all() 에서 호출시 pk 값의 활용법
    # id = tables.Column(accessor='pk', localize=False)
    # id = tables.Column(empty_values=()) # 객체의 갯수값 index 값
    # def __init__(self, *args, **kwargs):
    #     super(SimpleCountryTable, self).__init__(*args, **kwargs)
    #     self.counter = itertools.count()

    tz         = tables.Column(verbose_name='time zone')

    # list to dict 중 적용필드를 지정
    # name       = tables.Column(attrs=ATTRIBUTES)
    name       = tables.Column(footer='합계:')

    # lambda 함수로 합계 계산하기
    # population = tables.Column(footer=lambda table: sum(x['population'] for x in table.data))
    population = SummingColumn()


    visits     = tables.Column()
    # summary 컬럼 정렬시, 우선적 정렬 기준컬럼을 정의한다
    summary    = tables.Column(order_by=("name", "population"))
    # 컬럼명이 한글인 경우 한글객체도 가능 (근데 좀 찜찜함)
    참고자료   = tables.Column(accessor='기타')

    # buttons    = tables.TemplateColumn(template_name= "excel/people3.html",
    #                                    exclude_from_export=True)

    # 필터 조건함수
    # filterset_class = SimpleFilter


    # https://django-tables2.readthedocs.io/en/latest/pages/api-reference.html#table-meta
    class Meta:

        attrs = {'class': 'paleblue', 'width': '50%' }
        # template_name = 'django_tables2/bootstrap.html'
        template_name = 'django_tables2/bootstrap-responsive.html'
        # 위의 컬럼 정렬순서를 바꿀 때 (그냥 알아두자)
        sequence = ('name', 'tz', 'population', 'summary','visits', '참고자료')

        # 사용자 정의 템플릿을 사용 가능하다
        # 테이블 인스턴스에 in-line으로 추가 가능
        # table = PersonTable(data, template_name='django_tables2/bootstrap-responsive.html')
        # Basic : django_tables2/table.html
        # bootstrap 3 : django_tables2/bootstrap.html
        # bootstrap 4 : django_tables2/bootstrap4.html
        # .table-responsive : django_tables2/bootstrap-responsive.html
        # semantic UI : django_tables2/semantic.html




    # 하지만 페이지별 모든 테이블에 반복적 출력된다
    # 때문에 데이터에 포함은 되지 않음에 유의
    # 테이블 맨 위에 내용을 추가한다
    def get_top_pinned_data(self):
        return [
            {'name': 'usaA',
             'population': 8000,
             'tz': 'USA/NewYork',
             # 'visits': 12222,
             'summary': 'nice place',
             '기타': '어쩌고 탑'},
        ]

    # 테이블 맨 아래에 내용을 추가한다
    def get_bottom_pinned_data(self):
        return [
            {'name': 'usaZ',
             'population': 1111,
             'tz': 'USA/NewYork',
             # 'visits': 12222,
             'summary': 'nice place',
             '기타': '어쩌고 바텀'},
        ]



# 테이블 데이터 인스턴스
class PersonTable(tables.Table):
    class Meta:
        model = People




# Excel 파일을 열 때에는 xlrd 모듈만 있으면 되고
# 가공 및 저장시에는 openpyxl 모듈을 필요로 한다
import pandas as pd
import itertools

def check_xls(file, info=False):
    # 전체 9개 인덱스 동일내용이 있으면 1) 유효 헤더값, 2) 엑셀파일 내용 확인 모두 진행
    check_list = {
        "SEM": ['가맹점번호','매입사','승인번호','원거래일자','할부',
                '입금예정액','입금예정일자','정산상태','카드번호',],
    }

    # 헤더와 인덱스 자동생성 없이 순수한 엑셀파일 불러오기
    data = pd.read_excel(file, header=None, index_col=None)

    # 유효한 컬럼값 확인
    for i_col in range(5):
        valid_data = len(data.iloc[:, i_col].dropna())
        if valid_data != 0:
            endline_col = len(data.iloc[:, i_col].dropna())
            if info: print("{} 컬럼 {} 인덱스를 갖다".format(i_col, endline_col))
            break

    # 헤더값 확인하여 컬럼에 사용할 인덱스값과, 문서의 종류 확인하기
    for i in range(7):
        source_data = list(set(list(data.iloc[i, :].dropna())))
        for check in check_list.keys():
            # valid 이상 유효 값 존재여부 확인
            check_count, valid = 0, int(len(check_list[check]) / 2)
            check_data = check_list[check]
            checking = list(map(lambda x: x[0] == x[1],
                                itertools.product(source_data, check_data)))
            if sum(checking) > valid:
                end_i = i  # 이거없이 출력하면 7만 추출(break는 1번의 for만 탈출가능하다)
                if info:
                    print("{} 데이터의 유효컬럼은 {} 입니다".format(check, end_i))
                break

    # 출력본 수정1 : 컬럼수정
    col_names    = data.iloc[ end_i , :]
    data.columns = col_names
    # 출력본 수정2 : 유효한 값 추출 (컬럼값 + 1, 인덱스값 )
    # endline_col+1 이 없으면 테이블 아래 다른 자료도 출력
    data = data.iloc[end_i + 1:  endline_col + 1, i_col:].reset_index()
    data = data.drop(columns='index')

    # 중복컬럼이 존재 (해결할 필요가 존재)
    col_name = data.columns
    temp = {}  # 개별 객체의 중복갯수 카운트
    rename = []  # 새로운 컬럼명
    for no, col in enumerate(col_name):
        if no == 0:
            temp[col] = 1
            rename.append(col)
        else:
            if col not in temp:
                temp[col] = 1
                rename.append(col)
            else:
                temp[col] += 1
                col = col + str(temp[col])
                rename.append(col)
    data.columns = rename

    # 컬럼의 숫자 이지만 단위표시는 예외
    filtering_column = ['고객ID', '발급사', '승인번호', '가맹점번호']
    for col_name in data.columns:
        try:
            data[col_name] = data[col_name].astype(int)
            if col_name not in filtering_column:
                data[col_name] = data[col_name].apply("{:,}".format)
        except:
            pass
    return data, check # DataFrame, 이름
