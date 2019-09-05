from django import forms

from .models import UploadFileModel


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')
#이름이랑 파일
   # def __init__(self, *args, **kwargs):
   #      super(PostForm, self).__init__(*args, **kwargs)
   #     self.fields['file'].required = False
