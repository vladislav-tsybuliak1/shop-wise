from decimal import Decimal

from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    UNITS = (
        ("KG", "kilograms"),
        ("G", "grams"),
        ("L", "liters"),
        ("ML", "Milliliters"),
        ("PCS", "pieces"),
        ("BOX", "box")
    )

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_value = models.FloatField()
    unit_name = models.CharField(max_length=3, choices=UNITS)
    stock_quantity = models.FloatField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return f"{self.name} - {self.unit_value} {self.unit_name}"


class Order(models.Model):
    STATUSES = [
        ("PENDING", "The order is placed"),
        ("PROCESSING", "The order is being prepared"),
        ("SHIPPED", "The order is on the way to the customer"),
        ("DELIVERED", "The order has been delivered"),
        ("RETURNED", "The order was returned"),
        ("CANCELED", "The order was canceled")
    ]
    customer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=23, choices=STATUSES, default=STATUSES[0])
    products = models.ManyToManyField(to=Product, related_name="orders", through="OrderItem")

    class Meta:
        ordering = ("-created_at", )

    def __str__(self) -> str:
        return str(self.id)

    @property
    def total_cost(self) -> float:
        return sum(order_item.total_cost for order_item in self.order_items.all())


class OrderItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="order_items")
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.FloatField(default=1.0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["product", "order"], name="unique_order_product"),
        ]

    @property
    def total_cost(self) -> Decimal:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.product}: {self.quantity}"


class Review(models.Model):
    customer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ("-created_at", )

    def __str__(self) -> str:
        return f"By {self.customer.name} on {self.product}"


class ShoppingCart(models.Model):
    customer = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shopping_cart"
    )

    def __str__(self) -> str:
        return f"Shopping cart of {self.customer}"

    @property
    def total_cost(self) -> float:
        return sum(cart_item.total_cost for cart_item in self.cart_items.all())


class CartItem(models.Model):
    shopping_cart = models.ForeignKey(
        to=ShoppingCart,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    quantity = models.FloatField(default=1.0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["shopping_cart", "product"],
                name="unique_cart_product"
            )
        ]

    @property
    def total_cost(self) -> Decimal:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"{self.product}: {self.quantity}"
