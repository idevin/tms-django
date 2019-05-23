from django import forms


class AviaForm(forms.Form):
    avia_name = forms.CharField(label='имя', max_length=100)
    avia_from = forms.CharField(label='откуда', max_length=100)
    avia_to = forms.CharField(label='куда', max_length=100)
    avia_passengers = forms.IntegerField(label='количество человек')
    avia_date = forms.DateField(label='дата')
