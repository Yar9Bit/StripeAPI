from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View, TemplateView, ListView
import stripe

from stripe_api.models import Item

stripe.api_key = settings.STRIPE_SECRETE_KEY


class StripeView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': item.currency,
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "item_id": item.id
            },
            mode='payment',
            success_url=settings.YOUR_DOMAIN + 'success/',
            cancel_url=settings.YOUR_DOMAIN + 'cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemPageView(ListView):
    template_name = 'landing.html'
    model = Item
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = self.request.POST.get('val', 1)
        item = get_object_or_404(Item, id=item_id)
        context.update(
            {
                "item": item,
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
            }
        )
        return context
