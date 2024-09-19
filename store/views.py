from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from store.forms import ReviewForm
from store.models import (
    Product,
    Order,
    Brand,
    ShoppingCart,
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
    paginate_by = 5


class ProductDetailView(generic.DetailView):
    model = Product
    queryset = Product.objects.select_related("brand", "category").prefetch_related("reviews__customer")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["review_form"] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        review_form = ReviewForm(request.POST)
        product = self.get_object()
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.customer = request.user
            review.product = product
            review.save()
            return redirect("store:product-detail", pk=product.pk)
        context = self.get_context_data()
        context["review_form"] = review_form
        return self.render_to_response(context)


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 5
    queryset = Order.objects.prefetch_related("order_items__product")


class OrderDetailView(generic.DetailView):
    model = Order
    queryset = Order.objects.prefetch_related("order_items__product")


def cart_detail(request: HttpRequest) -> HttpResponse:
    cart, created = ShoppingCart.objects.get_or_create(customer=request.user)
    cart_items = cart.cart_items.select_related("product")
    total_cost = sum(item.quantity * float(item.product.price) for item in cart_items)
    context = {
        "cart": cart,
        "cart_items": cart_items,
        "total_cost": total_cost,
    }
    return render(request, "store/cart_detail.html", context=context)
