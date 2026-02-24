from django.views.generic import CreateView
from store.models import OwnCompany
from django.urls import reverse_lazy
from store.forms import OwnCompanyCreationForm

class OwnCompanyCreateView(CreateView):
    model = OwnCompany
    form_class = OwnCompanyCreationForm
    template_name = 'store/owncompanyadd.html'#!!!
    success_url = reverse_lazy('owncompanylist')

    def form_valid(self,form):
        return super().form_valid(form)