from django import forms
from django.utils.translation import gettext_lazy as _


class Question(forms.Form):

    the_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('The Date'),
            },
        ),
        label=_('The Date'),
    )
