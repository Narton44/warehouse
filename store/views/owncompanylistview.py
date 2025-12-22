from django.views.generic import ListView
from store.models import OwnCompany

class OwnCompanyListView(ListView):
    model = OwnCompany
    template_name = 'store/own_company_list.html'
    context_object_name = 'owncompany_list'