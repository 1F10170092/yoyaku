from django import forms


class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    tel = forms.CharField(max_length=30, label='年齢')
    remarks = forms.CharField(label='性別と症状', widget=forms.Textarea())