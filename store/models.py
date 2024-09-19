from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField(null=True)

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
    description = models.TextField(null=True)
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
