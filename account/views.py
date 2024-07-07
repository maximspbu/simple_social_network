from django.http import HttpResponse
from django.views import generic

from .models import Account


class IndexView(generic.ListView):
    template_name = "account/index.html"
    model = Account
    context_object_name = "account_list"

    def get_queryset(self):
        return Account.objects.order_by("-id")[:10]
    

class DetailView(generic.DetailView):
    template_name = "account/detail.html"
    model = Account

