from datetime import datetime
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import *


class ExpensesForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())

    class Meta:
        model = Expenses
        widgets = {'amount': forms.TextInput, 'name': forms.TextInput(attrs={'autofocus':'autofocus'})}


class IncomesForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())

    class Meta:
        model = Incomes
        widgets = {'amount': forms.TextInput}


class ReservesForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())

    class Meta:
        model = Reserves
        widgets = {'amount': forms.TextInput, 'name': forms.TextInput(attrs={'autofocus':'autofocus'})}


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Category


class ReportForm(forms.Form):
    start_date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())
    end_date = forms.DateField(widget=SelectDateWidget(years=range(2013, 2023, 1)), initial=datetime.today())
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.start_date, self.end_date, self.category)



