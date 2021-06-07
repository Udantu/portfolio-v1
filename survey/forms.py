from django import forms

class AnswerQuestion(forms.Form):
    answer = forms.IntegerField()
