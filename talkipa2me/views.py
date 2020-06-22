import environ
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView
from os import path
from talkipa2me.forms import IndexForm, IssuesForm
from talkipa2me.methods import eng_to_ipa

ROOT = environ.Path(__file__).path('../' * 2)
ENV = environ.Env(DJANGO_DEBUG=(bool, False), )
if path.isfile(ROOT('.env')):
    environ.Env.read_env(ROOT('.env'))
EMAIL_HOST_USER = ENV('EMAIL_HOST_USER')

class Index(FormView):
    form_class = IndexForm
    template_name = 'index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        text = self.request.POST.get('text_area')
        ipa = eng_to_ipa(text)
        return self.render_to_response(self.get_context_data(text=ipa))


class Issues(FormView):
    form_class = IssuesForm
    template_name = 'issues.html'
    success_url = reverse_lazy('issues')

    def form_valid(self, form):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        message = self.request.POST.get('message')
        send_mail(f"{name}: {email}", message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
        return self.render_to_response(self.get_context_data(answer=name.split()[0]))
