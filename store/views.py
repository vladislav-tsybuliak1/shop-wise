from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from store.models import (
    Product,
    Order,
    Brand,
)


def index(request: HttpRequest) -> HttpResponse:
    num_customers = get_user_model().objects.count()
    num_products = Product.objects.count()
    num_brands = Brand.objects.count()
    num_orders = Order.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_customers": num_customers,
        "num_products": num_products,
        "num_brands": num_brands,
        "num_orders": num_orders,
        "num_visits": num_visits + 1,
    }

    return render(request, "store/index.html", context=context)


class ProductListView(generic.ListView):
    model = Product
