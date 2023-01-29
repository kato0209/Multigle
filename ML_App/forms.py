from django import forms
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):

    keyword = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['keyword'].widget.attrs.update({'class' : 'form-control','placeholder':'キーワードを入力してください'})