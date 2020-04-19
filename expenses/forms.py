from django import forms

class ExpenseForm(forms.Form):
	date = forms.DateField(label='When did you kurban?')
	name = forms.CharField(label='What did you spend the money on?', max_length=100)
	category = forms.CharField(label='What Category does it fall under?', max_length=100)
	tax = forms.FloatField(label='How much money kurban to govt?')
	tip = forms.FloatField(label='How much money kurban to the shop?')
	total = forms.FloatField(label='So total how much kurban?')
	comments = forms.CharField(label='Any safai?', max_length=100)
