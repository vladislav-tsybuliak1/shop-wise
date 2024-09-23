from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Case, When, IntegerField, QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from store.forms import ReviewForm, CustomerCreationForm, OrderStatusForm, SearchForm, ProductFilterForm
from store.models import (
    Product,
    Order,
    Brand,
    ShoppingCart,
    CartItem,
    Category, OrderItem,
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


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = SearchForm(self.request.GET,
            initial={
                "name": name,
            }
        )
        context["filter_form"] = ProductFilterForm(self.request.GET)
        context["cart_items"] = {
            item.product_id: item.quantity
            for item
            in self.request.user.shopping_cart.cart_items.all()
        }

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Product.objects.annotate(
            available=Case(
                When(stock_quantity__gt=0, then=1),
                default=0,
                output_field=IntegerField(),
            )
        ).select_related("brand", "category").order_by("-available", "name")

        search_form = SearchForm(self.request.GET)
        filter_form = ProductFilterForm(self.request.GET)

        if search_form.is_valid():
            queryset = queryset.filter(
                name__icontains=search_form.cleaned_data["name"]
            )

        if filter_form.is_valid():
            brand = filter_form.cleaned_data.get("brand")
            category = filter_form.cleaned_data.get("category")

            if brand:
                queryset = queryset.filter(brand=brand)
            if category:
                queryset = queryset.filter(category=category)

        return queryset


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    queryset = Product.objects.select_related("brand", "category").prefetch_related("reviews__customer")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["review_form"] = ReviewForm()
        context["cart_items"] = {
            item.product_id: item.quantity
            for item
            in self.request.user.shopping_cart.cart_items.all()
        }
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


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse("store:product-detail", args=[self.object.pk])


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse("store:product-detail", args=[self.object.pk])


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy("store:product-list")


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    paginate_by = 5
    queryset = Order.objects.prefetch_related("order_items__product", "customer")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["status_form"] = OrderStatusForm()
        return context


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    queryset = Order.objects.prefetch_related("order_items__product", "customer")


class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = SearchForm(self.request.GET,
            initial={
                "name": name,
            }
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Category.objects.all()
        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            queryset = queryset.filter(
                name__icontains=search_form.cleaned_data["name"]
            )
        return queryset


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("store:category-list")


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("store:category-list")


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy("store:category-list")


class BrandListView(LoginRequiredMixin, generic.ListView):
    model = Brand
    paginate_by = 5
    queryset = Brand.objects.prefetch_related("products")


class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("store:brand-list")


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("store:brand-list")


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    success_url = reverse_lazy("store:brand-list")


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    paginate_by = 5
    queryset = get_user_model().objects.prefetch_related("orders")


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["order_list"] = self.get_object().orders.select_related("customer").prefetch_related("order_items__product")
        return context


class CustomerCreateView(generic.CreateView):
    model = get_user_model()
    form_class = CustomerCreationForm

    def get_success_url(self) -> str:
        return reverse("store:customer-detail", args=[self.object.pk])


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    fields = ["first_name", "last_name", "phone_number", "address"]

    def get_success_url(self) -> str:
        return reverse("store:customer-detail", args=[self.object.pk])


class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("store:customer-list")


@login_required
def cart_detail(request: HttpRequest) -> HttpResponse:
    shopping_cart, created = ShoppingCart.objects.get_or_create(customer=request.user)
    cart_items = shopping_cart.cart_items.select_related("product")
    total_cost = sum(item.quantity * float(item.product.price) for item in cart_items)
    context = {
        "shopping_cart": shopping_cart,
        "cart_items": cart_items,
        "total_cost": total_cost,
    }
    return render(request, "store/cart_detail.html", context=context)


@login_required
def add_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    product = get_object_or_404(Product, id=product_id)
    shopping_cart, created = ShoppingCart.objects.get_or_create(customer=request.user)
    cart_item = CartItem.objects.filter(shopping_cart=shopping_cart, product=product).first()
    if cart_item:
        if cart_item.quantity < product.stock_quantity:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Product quantity updated in the cart.")
        else:
            messages.warning(request, "Cannot add more of this product; not enough stock available.")
    else:
        if product.stock_quantity > 0:
            CartItem.objects.create(shopping_cart=shopping_cart, product=product, quantity=1)
            messages.success(request, "Product added to cart.")
        else:
            messages.warning(request, "This product is out of stock.")
    return redirect(request.META.get("HTTP_REFERER", reverse_lazy("store:index")))


@login_required
def delete_from_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    product = get_object_or_404(Product, id=product_id)
    shopping_cart = ShoppingCart.objects.get(customer=request.user)
    cart_item = CartItem.objects.get(shopping_cart=shopping_cart, product=product)

    full_delete = request.GET.get("full_delete")

    if full_delete:
        cart_item.delete()
        messages.success(request, "Product deleted from the cart.")
    else:
        cart_item.quantity -= 1
        if cart_item.quantity == 0:
            cart_item.delete()
            messages.success(request, "Product deleted from the cart.")
        else:
            cart_item.save()
            messages.success(request, "Product quantity updated in the cart.")
    return redirect(request.META.get("HTTP_REFERER", reverse_lazy("store:index")))


@login_required
def empty_cart(request: HttpRequest) -> HttpResponse:
    shopping_cart = ShoppingCart.objects.get(customer=request.user)
    shopping_cart.cart_items.all().delete()
    messages.success(request, "Shopping Cart was emptied.")
    return redirect("store:cart-detail")


@login_required
def update_order_status(request: HttpRequest, pk: int) -> HttpResponse:
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Order status updated.")
            return redirect("store:order-list")
    return redirect("store:order-list")


@login_required
def create_order_from_cart(request: HttpRequest) -> HttpResponse:
    shopping_cart = get_object_or_404(ShoppingCart, customer=request.user)
    cart_items = CartItem.objects.prefetch_related("product").filter(shopping_cart=shopping_cart)
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty. Please add items to your cart before placing an order.")
        return redirect("store:cart")

    with transaction.atomic():
        order = Order.objects.create(customer=request.user)
        added_items = 0
        for cart_item in cart_items:
            if cart_item.quantity > cart_item.product.stock_quantity:
                cart_item.quantity = cart_item.product.stock_quantity
                messages.warning(request, f"The quantity {cart_item.quantity} of {cart_item.product.name} is available.")
            if cart_item.quantity > 0:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                )
                cart_item.product.stock_quantity -= cart_item.quantity
                cart_item.product.save()
                added_items += 1
        cart_items.delete()
        if added_items == 0:
            order.delete()
            messages.warning(request, f"Order wasn't placed because no product from the list is available is stock.")
            return redirect("store:cart-detail")
    messages.success(request, "Order is placed.")
    return redirect("store:order-detail", pk=order.id)
