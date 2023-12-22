from django.urls import path, include
from .views import SubscriptionList, SubscriptionCreate, SubscriptionDelete, SubscriptionUpdate

urlpatterns = [
    path('list/', SubscriptionList.as_view(), name='list'),
    path('create/', SubscriptionCreate.as_view(), name='create_subscription'),
    path('delete/<int:pk>', SubscriptionDelete.as_view(), name='delete'),
    path('update/<int:pk>', SubscriptionUpdate.as_view(), name='update')
]
