import os
from django import forms
from .models import Video, Comment


# Generate & ValidCheck the form data in here..
class VideoForm(forms.ModelForm):
    def clean_file(self):
        # self.cleaned_data : read the file name passing the validation check.
        file = self.cleaned_data.get("file", None)
        if file:
            extension = os.path.splitext(file.name)[-1].lower()
            if extension not in [".mp4", ".avi", ".mkv", ".mov"]:
                raise forms.ValidationError("file extension is not avaliable to Use")
            else:
                pass
        else:
            return file

    class Meta:
        model = Video
        fields = ["title", "description", "file", "photo"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {"content": forms.Textarea(attrs={"rows": 3})}

