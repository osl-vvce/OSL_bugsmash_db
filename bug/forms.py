from django import forms


class db_form(forms.Form):

    CHOICES = [
        ('last_name', 'first_name'),
        ('first_name', 'last_name'),
        ('phone', 'email'),
        ('email','phone'),
        ('gender','gender'),
        ('salary','salary')
    ]
    column_name = forms.ChoiceField(label='column', choices=CHOICES)

