from django import forms


class IndexForm(forms.Form):
    text_area = forms.CharField(label="",
                                widget=forms.Textarea(
                                    attrs={'class': 'textarea is-primary',
                                           'placeholder': 'Over here!'}))
