from django import forms
from api.models import Problem


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        exclude = ['reported_by', 'date_of_creation','status','solution','resolved_user']


class SolutionForm(forms.Form):
    solution = forms.CharField()
