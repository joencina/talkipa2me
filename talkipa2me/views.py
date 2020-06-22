from django.urls import reverse_lazy
from django.views.generic import FormView

from talkipa2me.forms import IndexForm, IssuesForm
from talkipa2me.methods import eng_to_ipa


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
        return self.render_to_response(self.get_context_data(answer=text))
