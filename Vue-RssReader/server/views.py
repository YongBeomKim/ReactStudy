from django.views.generic.base import TemplateView
from django.shortcuts import render
from .apexjson import apex_linebar, apex_candle_vol, apexSamples, stock_data


class HomeView(TemplateView):
    template_name = 'home.html'


def home(request):

    _, dataframe_data = apexSamples()
    # data = stock_data('005930.KS')

    content = {
        "chartdata": apex_linebar(dataframe_data, types='area', stacked=True, curve='smooth'),
        # "chartdata": apex_candle(data),
        # 'optionsCandlestick' : data,
        # 'options' : vol,
    }
    return render(request, "home.html", content)


# Json 데이터를 API로 넘길 떄 csrf 보안내용을 추가합니다
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.http import JsonResponse


# https://stackoverflow.com/questions/49477585/django-react-axios
# Api를 Post로 전송하도록 보안을 추가합니다
@method_decorator(csrf_protect)
def index(self, request):
    data = apex_linebar(dataframe_data, types='area', stacked=True, curve='smooth', output=True)
    print(data)
    return JsonResponse(data)

def export_json(request):
    data = apex_linebar(dataframe_data, types='area', stacked=True, curve='smooth', output=True)
    return JsonResponse(data)