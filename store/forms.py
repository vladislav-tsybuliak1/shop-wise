from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from store.models import Review


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