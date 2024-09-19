from django import forms

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
