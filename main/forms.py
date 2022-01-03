from django import forms

class CryptocurrencyForm(forms.Form):
	cryptocurrency = forms.ChoiceField(label='', choices=[('BTC', 'BTC'), ('ETH', 'ETH'), ('LTC', 'LTC')],  widget=forms.Select(attrs={'class': 'form-control mr-sm-2', 'name': 'cryptocurrency'}),)
	period = forms.ChoiceField(label='', choices=[(1, '1 day'), (7, '7 days'), (30, '30 days')], widget=forms.Select(attrs={'class': 'form-control mr-sm-2', 'name': 'period'}),)
	style =  forms.ChoiceField(label='', choices=[('Line chart', 'Line chart'), ('Bar chart', 'Bar chart'), ('Table', 'Table')], widget=forms.Select(attrs={'class': 'form-control mr-sm-2', 'name': 'style'}),)
