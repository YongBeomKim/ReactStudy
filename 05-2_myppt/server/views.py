from django.shortcuts import render
from django.http import JsonResponse


def works(request):
    markdown = (
        "### <small>근무이력</small> **Yong Beom Kim**\n"
        + "<br/>\n"
        + "\n"
        + "2005.06 ~ 2007.01 : **대우일렉트로닉스** 홈오토메이션 UI / UX\n"
        + "<br/>\n"
        + "\n"
        + "2009년 **무영인터내쇼날 두산벤처다임** 구내식당\n"
        + "<br/>\n"
        + "\n"
        + "2018년 **삼성전자 서울캠퍼스** 딥러닝 자연어 강사\n"
        + "<br/>\n"
        + "\n"
        + "2019년 **4차 산업 예비창업패키지** 선정 (중소기업부 창진원)\n"
        + "<br/>\n"
        + "\n"
        + "- **[만능식판](https://sikpan.kr)** 서비스 시작\n"
        + "- 식단 데이터 생성 및 그 장치 **(출원번호 : 10-2020-0036441)**\n"
        + "- K-ICT 빅데이터 센터 (판교) / 분석용 H/W 지원 / 2019.10\n"
        + "- 2019년 하반기 경기도경제과학진흥원 클라우드 지원 / 2020.01\n"
    )
    content = {
        # "content": markdown,
    }
    return render(request, "works.html", content)


def profile(request):
    markdown = (
        "### <small>근무이력</small> **Yong Beom Kim**\n"
        + "<br/>\n"
        + "\n"
        + "2005.06 ~ 2007.01 : **대우일렉트로닉스** 홈오토메이션 UI / UX\n"
        + "<br/>\n"
        + "\n"
        + "2009년 **무영인터내쇼날 두산벤처다임** 구내식당\n"
        + "<br/>\n"
        + "\n"
        + "2018년 **삼성전자 서울캠퍼스** 딥러닝 자연어 강사\n"
        + "<br/>\n"
        + "\n"
        + "2019년 **4차 산업 예비창업패키지** 선정 (중소기업부 창진원)\n"
        + "<br/>\n"
        + "\n"
        + "- **[만능식판](https://sikpan.kr)** 서비스 시작\n"
        + "- 식단 데이터 생성 및 그 장치 **(출원번호 : 10-2020-0036441)**\n"
        + "- K-ICT 빅데이터 센터 (판교) / 분석용 H/W 지원 / 2019.10\n"
        + "- 2019년 하반기 경기도경제과학진흥원 클라우드 지원 / 2020.01\n"
    )
    content = {
        "content": markdown,
    }
    return render(request, "profile.html", content)


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
        "### <small>portfolio of</small> **Yong Beom Kim**\n"
        + "\n"
        + "<br/>\n"
        + "\n"
        + "- **[Github](https://github.com/wsvincent/djangoforapis_30)**\n"
        + "<br/>\n"
        + "\n"
        + "- **[만능식판](http://sikpan.kr)**\n"
        + "<br/>\n"
        + "\n"
        + "- **[딥러닝 강의 Slide Share](https://www.slideshare.net/YBkim2)**\n"
        + "<br/>\n"
        # + "```python\n"
        # + "@register.filter()\n"
        # + "@stringfilter\n"
        # + "def markdown(value):\n"
        # + "    return md.markdown(\n"
        # + '        value, extensions=["markdown.extensions.fenced_code"]\n'
        # + ")\n"
        # + "```\n"
    )

    content = {
        "props": props,
        "js_app_name": js_app_name,
        "content": markdown,
    }
    return render(request, "index.html", content)
