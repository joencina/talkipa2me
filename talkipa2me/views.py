from django.urls import reverse_lazy
from django.views.generic import FormView

from forms import IndexForm


class Index(FormView):
    form_class = IndexForm
    template_name = 'index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        text = self.request.POST.get('text_area') * 2
        return self.render_to_response(self.get_context_data(text=text))
