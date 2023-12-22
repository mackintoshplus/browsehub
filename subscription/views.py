from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Subscription
from django.urls import reverse_lazy    

# Create your views here.


class SubscriptionList(ListView):
    template_name = "list.html"
    model = Subscription


class SubscriptionCreate(CreateView):
    template_name = "create.html"
    model = Subscription
    fields = ('magazine_name', 'link', 'monthly_fee', 'priority')
    success_url = reverse_lazy('list')

class SubscriptionDelete(DeleteView):
    template_name = "delete.html"
    model = Subscription
    success_url = reverse_lazy('list')

class SubscriptionUpdate(UpdateView):
    template_name = "update.html"
    model = Subscription
    fields = ('magazine_name', 'link', 'monthly_fee', 'priority')
    success_url = reverse_lazy('list')