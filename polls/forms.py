from django import forms
from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'time_pub', )
        # widgets = {
        #     'question_text': forms.TextInput(attrs={'class': 'question'}),
        #     'time_pub': forms.TextInput(attrs={'class': 'time'})
        # }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
