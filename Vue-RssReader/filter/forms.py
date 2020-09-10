from django import forms
from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Snippet

# 셀 2개를 다루는 위젯을 정의합니다
class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['',''] # 초기값 지정


class NameField(forms.MultiValueField):

    widget = NameWidget # 셀2개로 분리된 위젯을 사용

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[가-힣]+', '한글입력')]), # test
            forms.CharField(validators=[
                RegexValidator(r'[가-힣]+', '한글입력')]), # none
        )
        super().__init__(fields, *args, **kwargs)

    # 2개의 위젯 셀을 1개로 압축출력 합니다
    def compress(self, data_list):
        # data_list = ['first_value', 'second_value']
        return f'{data_list[0]} {data_list[1]}'


# form 에서만 임시로 관리팔 필드를 정의
class ContactForm(forms.Form):
    name     = NameField()
    email    = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[('question', '검색'),('test', '검사'), ('other','기타')])
    subject  = forms.CharField(required=False)
    body     = forms.CharField(widget=forms.Textarea) # 주요 Message

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_show_errors = True

        # form 객체의 layout 스타일을 정의한다
        self.helper.layout = Layout(
            'name', 'email', 'category', 'subject', 'body',
            Submit('submit', '전송하기', css_class='btn-success')
        )



# Snippet 모델과 연결할 데이터를 정의
class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'body')
