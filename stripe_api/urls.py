from django.urls import path
from .views import StripeView, SuccessView, CancelView, ItemPageView

urlpatterns = [
    path('buy/<pk>/', StripeView.as_view(), name='stripe_view'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', ItemPageView.as_view(), name='item_page'),
]
