from django import forms


class QuizForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    print('hi')
