from django import forms


class IndexForm(forms.Form):
    widget = forms.Textarea(attrs={'class': 'textarea is-primary', 'placeholder': 'Over here!'})
    text_area = forms.CharField(label="", widget=widget)


class IssuesForm(forms.Form):
    textarea_widget = forms.Textarea(attrs={'class': 'input', 'type': 'text', 'placeholder': 'Your name'})
    name = forms.CharField(max_length=200, widget=textarea_widget)

    email_input = forms.EmailInput(attrs={'class': 'input', 'type': 'email', 'placeholder': 'example@gmail.com'})
    email = forms.EmailField(max_length=200, widget=email_input)

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Your message'}))
