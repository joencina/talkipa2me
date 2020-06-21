from django.urls import reverse_lazy
from django.views.generic import FormView

from talkipa2me.forms import IndexForm
from talkipa2me.methods import eng_to_ipa

class Index(FormView):
    form_class = IndexForm
    template_name = 'index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        text = self.request.POST.get('text_area')
        ipa = eng_to_ipa(text)
        return self.render_to_response(self.get_context_data(text=ipa))
