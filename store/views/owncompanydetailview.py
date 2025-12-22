from django.views.generic import DetailView
from store.models import OwnCompany

class OwnCompanyDetailView(DetailView):
    model = OwnCompany
    template_name = 'store/owncompany_detail_view.html'
    context_object_name = 'owncompany'