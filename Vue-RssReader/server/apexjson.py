import random, json
import pandas as pd
from pandas_datareader import get_data_yahoo
from datetime import date, datetime


def set_default(obj):

    r"""
    Object의 유효여부를 확인

    :param obj: 확일할 객체
    :return: Type Error Check Result
    """

    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def json_serial(obj):

    r"""
    시계열 데이터의 유효여부를 확인

    :param obj: 확인할 객체
    :return:
    """

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def apexSamples():

    # Sample DataSet
    keys        = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
    data_value  = [10, 41, 35, 51, 49, 62, 69, 91, 148]
    series_data = { key : data_value[no]   for no, key in enumerate(keys)}
    series_data = pd.Series(series_data)
    series_data.name = 'Desktop'

    dataframe_data = pd.DataFrame()
    for col in ['col1', 'col2', 'col3'] :
        random.shuffle(data_value)
        dataframe_data[col] = data_value
    return series_data, dataframe_data


def stock_data(code, start_date='2018-01-01', end_date='2018-12-31', time=True):

    r"""
    샘플 주가데이터를 생성합니다
    :param code: (str) 기업코드 ex) 005930.ks
    :param start_date: (str) 수집시작일 ex) '2018-01-01'
    :param end_date: (str) 수집종료일 ex) '2018-12-31'
    :param time: (boolean) 시간데이터 추가여부 (장 마감시간)
    :return: DataFrame (pandas)
    """

    df = get_data_yahoo(code, start_date, end_date)
    df = df.iloc[:, :-1]
    for col in df.columns:
        df[col] = df[col].astype(int)
    df      = df.reset_index()
    # Json 타입으로 시간자료를 바꾸고, 장 마감시간을 추가합니다
    df.Date = list(map(lambda x: json_serial(x), df.Date))
    if time:
        df.Date = list(map(lambda x: x.replace("T00:00:00", "T15:30:00"), df.Date))
    return df


# Pandas 객체를 Json으로 변환출력합니다
# import pandas as pd
# import json

# 시리즈 데이터는 무조건 [List / Array]로 둘러싸여야 한다
# series: [
#     {name: "Desktops",
#      data: [10, 41, 35, 51, 49, 62, 69, 91, 148]}
# ],

# types (str)    : 'line', 'bar', 'area'(하위 영역 색표시)
# zoom (boolean) : 부분 확장기능 활성화 여부
# marker (int)   : 개별 포인팅 크기
# stacked (boolean) : 여러 데이터를 적층여부
# curve (str) : 데이터 자료간 보간방법
# title, title_font (str) : 차트의 제목

def apex_linebar(data, types='line', zoom='False', height=350, marker=0,
                 stacked = True, data_label=True, curve='straight',
                 title='None', title_font='14px', output=False):

    r"""
    apexchart 기본포맷(막대/선차트) json을 출력
    :param data: Raw data
    :param types: (str) bar/line
    :param zoom: (boolean)
    :param height: (int) 높이값 설정
    :param marker: (int) point 의 marker 크기
    :param stacked: (boolean) 다른 필드의 값을 적층 여부
    :param data_label: (boolean)
    :param curve: (str) 'straight', 'smooth'
    :param title: (str) 'text of title'
    :param title_font: (str) title font size ex)'14px'
    :param output: (boolean)
    :return: json
    """

    # data type is Series
    if type(data) == pd.core.series.Series :
        data_set = {}
        data_set["name"] = data.name
        data_set["type"] = types
        data_set["data"] = data.values.tolist()
        data_set         = [data_set]

    # data type is DataFrame
    elif type(data) == pd.core.frame.DataFrame :

        # 스타일을 석는경우 종류를 구분하여 출력
        data_set, raw_data = [], data.to_dict(orient='list')
        for key in raw_data.keys():
            temp_dict = {}
            temp_dict['name'] = key
            temp_dict["type"] = types
            temp_dict['data'] = raw_data[key]
            data_set.append(temp_dict)
    else:
        print('You Need to Convert to Pandas Dataset')
        return None

    # Common Elements
    options = {
        "chart": {
            "height"  : height,
            "stacked" : stacked,
            "toolbar" : {"show"   : False},
            "zoom"    : {"enabled": zoom}
        },
        "plotOptions" : {
            "bar" : {
                "dataLabels" : {
                    "position": 'top', # top, center, bottom
                },
            }
        },
        # 개별 데이터 포인트에 대한 마커를 표시합니다
        "dataLabels": {
            # "formatter" : "function(val) {return val + '%'};",
            "enabled": data_label,
            "style" : {
                "fontSize" : '15px',
                # "colors"   : ["#304758"]
            },
            "dropShadow" : {
                "enabled" : True
            },
            #"formatter": False,  # function(val,opt){return opt.w.globals.labels[opt.dataPointIndex]+":"+val},
        },
        "stroke": {"curve": curve},
        "title": {
            "text": title,  # Chart Title
            "align": 'left',
            "style": {
                "fontSize": title_font
            },
        },
        "grid": {
            "row": {
                "colors": ['#f3f3f3', 'transparent'],
                "opacity": 0.5
            },
        },
        "markers": {
            "size": marker,
            "hover": {"sizeOffset": 2}
        },
        # 데이터 입력
        "series": data_set,
        "xaxis": {
            "categories": data.index.tolist(),
        },
    }
    if output == True:
        return options
    return json.dumps(options)


def apex_candle(data, height=350, marker=0,
                 stacked = True, data_label=True, curve='straight',
                 title='None', title_font='14px'):

    r"""
    apexchart's 의 캔들차트 데이터를 생성합니다
    :param height: (int)
    :param title: (str)
    :param title_font: (str)
    :return:
    """
    # data  = stock_data('005930.KS')

    try:
        df_summary = data[['Date', 'Open', 'High', 'Low', 'Close']]
    except:
        return "this is not a Stock data"

    dataset, raw_data = [], df_summary.to_dict(orient='split')['data']
    for col_data in raw_data:
        result      = {}
        result["x"] = col_data[0]
        result["y"] = col_data[1:]
        dataset.append(result)

    # Common Elements
    options = {
        "chart": {
            "height": height,
            "type": 'candlestick',
        },
        "title": {
            "text": title,  # Chart Title
            "align": 'left',
            "style": {
                "fontSize": title_font
            },
        },
        "xaxis": {  # 시계열 데이터를 입력합니다
            "type": 'datetime'
        },
        "yaxis": {
            "tooltip": {
                "enabled": True
            }
        },
        # "grid": {
        #     "row": {
        #         "colors": ['#f3f3f3', 'transparent'],
        #         "opacity": 0.5
        #     },
        # },
        # "markers": {
        #     "size": marker,
        #     "hover": {"sizeOffset": 2}
        # },
        "series": [{"data": dataset}],
    }
    return json.dumps(options)


def apex_candle_vol(data):

    r"""
    주가와 거래량 그래프 데이터를 생성합니다
    :param data: (DataFrame) 주가 데이터
    :return: json
    """

    # data = stock_data('005930.KS')
    try:
        df_summary = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    except:
        return "this is not a Stock data"

    raw_data   = df_summary.to_dict(orient='split')['data']
    seriesData = []
    for col_data in raw_data:
        result = {}
        result["x"] = col_data[0]
        result["y"] = col_data[1:-1]
        seriesData.append(result)

    # volume 데이터 생성하기
    seriesDataLinear = []
    for col_data in raw_data:
        result = {}
        result["x"] = col_data[0]
        result["y"] = col_data[-1]
        seriesDataLinear.append(result)

    # 캔들차트 그리기
    optionsCandlestick = {
        "chart": {
            "id": 'candles',
            "height": 290,
            "type": 'candlestick',
            "toolbar": {
                "autoSelected": 'pan',
                "show": False
            },
            "zoom": {"enabled": False},
        },
        "plotOptions": {
            "candlestick": {
                "colors": {
                    "upward": '#3C90EB',
                    "downward": '#DF7D46'
                }
            }
        },
        "series": [{"data": seriesData}],
        "xaxis": {"type": 'datetime'},
    }

    # 볼륨차트 그리기
    options = {
        "chart": {
            "height": 160,
            "type": 'bar',
            "brush": {
                "enabled": True,
                "target": 'candles'
            },
            "selection": {
                "enabled": True,
                "xaxis": {
                    "min: new Date('20 Jan 2017').getTime()",
                    "max: new Date('10 Dec 2017').getTime()"
                },
                "fill": {
                    "color": '#ccc',
                    "opacity": 0.4
                },
                "stroke": {
                    "color": '#0D47A1',
                }
            },
        },
        "dataLabels": {
            "enabled": False
        },
        "plotOptions": {
            "bar": {
                "columnWidth": '80%',
                "colors": {
                    "ranges": [
                        {"from": -1000,
                         "to": 0,
                         "color": '#F15B46'
                         }, {
                            "from": 1,
                            "to": 10000,
                            "color": '#FEB019'
                        }
                    ],
                },
            }
        },
        "stroke": {"width": 0},
        "series": [{
            "name": 'volume',
            "data": seriesDataLinear
        }],
        "xaxis": {
            "type": 'datetime',
            "axisBorder": {
                "offsetX": 13
            }
        },
        "yaxis": {
            "labels": {"show": False}
        }
    }
    return json.dumps(options, default=set_default), json.dumps(optionsCandlestick)