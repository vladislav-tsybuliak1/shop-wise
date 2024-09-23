from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from store.models import Review, Order, Brand, Category
from store.validators import validate_phone_number, validate_address


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("content", )
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 2,
                "placeholder": "Write your review here...",
            }),
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["content"].label = ""


class CustomerCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        validators=[validate_phone_number],
        max_length=13,
        widget=forms.TextInput(attrs={"placeholder": "+380XXXXXXXXX"})
    )

    address = forms.CharField(
        validators=[validate_address],
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Enter address'})
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
            if self.errors.get(field_name):
                field.widget.attrs["class"] += " is-invalid"


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("status",)


class SearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name..."
            }
        )
    )


class ProductFilterForm(forms.Form):
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        empty_label="All Brands"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories"
    )
