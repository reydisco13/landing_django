from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True)
    from_email = forms.EmailField(label='Email', required=True)
    number = forms.CharField(label='Номер телефона', max_length=12, required=True)
