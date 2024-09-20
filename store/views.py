from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from store.forms import ReviewForm
from store.models import (
    Product,
    Order,
    Brand,
    ShoppingCart,
    CartItem,
    Category,
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


class ProductCreateView(generic.CreateView):
    model = Product
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse("store:product-detail", args=[self.object.pk])


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 5
    queryset = Order.objects.prefetch_related("order_items__product")


class OrderDetailView(generic.DetailView):
    model = Order
    queryset = Order.objects.prefetch_related("order_items__product")


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 5


class CategoryCreateView(generic.CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("store:category-list")


class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("store:category-list")


class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy("store:category-list")


class BrandListView(generic.ListView):
    model = Brand
    paginate_by = 5
    queryset = Brand.objects.prefetch_related("products")


class BrandCreateView(generic.CreateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("store:brand-list")


class BrandUpdateView(generic.UpdateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("store:brand-list")


class BrandDeleteView(generic.DeleteView):
    model = Brand
    success_url = reverse_lazy("store:brand-list")


class CustomerListView(generic.ListView):
    model = get_user_model()
    paginate_by = 5
    queryset = get_user_model().objects.prefetch_related("orders")


class CustomerDetailView(generic.DetailView):
    model = get_user_model()

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["order_list"] = self.get_object().orders.all()
        return context



def cart_detail(request: HttpRequest) -> HttpResponse:
    shopping_cart, created = ShoppingCart.objects.get_or_create(customer=request.user)
    cart_items = shopping_cart.cart_items.select_related("product")
    total_cost = sum(item.quantity * float(item.product.price) for item in cart_items)
    context = {
        "cart": shopping_cart,
        "cart_items": cart_items,
        "total_cost": total_cost,
    }
    return render(request, "store/cart_detail.html", context=context)


def add_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    product = get_object_or_404(Product, id=product_id)
    shopping_cart, created = ShoppingCart.objects.get_or_create(customer=request.user)
    cart_item, created = CartItem.objects.get_or_create(shopping_cart=shopping_cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect(request.META.get("HTTP_REFERER", reverse_lazy("store:index")))