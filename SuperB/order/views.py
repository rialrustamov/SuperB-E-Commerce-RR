from order.models import CheckoutBilling, ShoppingCart
from django.shortcuts import render



# Create your views here.

from order.forms import CheckoutBillingForm

def quick_view(request):
    return render(request, 'quick_view.html')


def shopping_cart(request):
    return render(request, 'shopping_cart.html')


def wishlist(request):
    return render(request, 'wishlist.html')

def result(request):
    context = {
        'title': 'Result',
    }
    return render(request, 'result.html', context=context)


def checkout(request):
    context = {
        'title': 'Checkout',
    }
    return render(request, "checkout.html", context=context)


def checkout_bill(request):
    if request.method == "POST":
        form = CheckoutBillingForm(request.POST)
        if form.is_valid():
            shipping = CheckoutBilling(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                company=request.POST.get('company'),
                email=request.POST.get('email'),
                address=request.POST.get('address'),
                country=request.POST.get('country'),
                telephone=request.POST.get('telephone'),
                fax=request.POST.get('fax'),
                user_billing_info=request.user,
            )
            shipping.save()
            ShoppingCart.objects.filter(user=request.user).filter(is_ordered=False).update(is_ordered=True, shipping_address=shipping)
            ShoppingCart.objects.get_or_create(user=request.user, is_ordered=False)
    context = {
        'title': 'Checkout Billing',
        'form': CheckoutBillingForm
    }
    return render(request, "checkout_billing_info.html", context=context)
