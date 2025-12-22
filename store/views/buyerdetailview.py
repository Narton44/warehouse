from django.views.generic import DetailView
from store.models import Buyer

class BuyerDetailView(DetailView):
    model = Buyer
    template_name = 'store/buyer_detail_view.html'
    context_object_name = 'buyer'