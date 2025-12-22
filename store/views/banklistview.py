from django.views.generic import ListView
from store.models import Bank

class BankListView(ListView):
    model = Bank
    template_name = 'store/bank_list.html'
    context_object_name = 'bank_list'