from django import forms


class VinDecodeForm(forms.Form):
    vin_code = forms.CharField(label='VIN Code', max_length=17)
