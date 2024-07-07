from django.shortcuts import get_object_or_404, render
from django.views import generic


from .models import Account


class IndexView(generic.ListView):
    template_name = "account/index.html"
    model = Account
    context_object_name = "account_list"

    def get_queryset(self):
        return Account.objects.order_by("-id")
    

class DetailView(generic.DetailView):
    template_name = "account/detail.html"
    model = Account
