from django.views.generic import ListView
from store.models import Buyer

class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer_list'