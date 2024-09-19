from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name
