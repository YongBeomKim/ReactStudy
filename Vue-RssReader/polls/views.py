from django.shortcuts import render, render_to_response

# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # Question 테이블에서 question_id 인덱스를 추출하고
    # 해당 인덱스 값이 없으면 404 오류를 출력한다
    # Choice 테이블을 기준으로 가져올거 같은데, Question 기준으로 하는 이유는???
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {'question':question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})


def vote(request, question_id):
    #
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # Choice.DoesNotExist : 검색조건에 해당하는 값이 없을 때 출력
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            'question': question,
            'error_message':"선택한 내용이 없습니다"})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


# boken in Django

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


def plot_bokeh(request):

    x = [1,3,5,7,9,11,13]
    y = [1,2,3,4,5,6,7]
    title = 'y = f(x)'

    plot = figure(title= title ,
        x_axis_label= 'X-Axis',
        y_axis_label= 'Y-Axis',
        plot_width =400,
        plot_height =400)

    plot.line(x, y, legend= 'f(x)', line_width = 2)

    #Store components
    script, div = components(plot)
    content = {'script' : script , 'div' : div}

    #Feed them to the Django template.
    return render_to_response('polls/bokeh.html', content)
