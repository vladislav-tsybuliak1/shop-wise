import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_name(name: str) -> None:
    if re.search(r"^[a-zA-Z]*$", name) is None:
        raise ValidationError(
            f"{name} contains non-english letters"
        )


def validate_username(username: str) -> None:
    if re.search(r"^[a-zA-Z_]*$", username) is None:
        raise ValidationError(
            f"{username} contains non-english letters or characters other than underscore"
        )
    if username.startswith('_') or username.endswith('_'):
        raise ValidationError(f"{username} cannot start or end with an underscore")


def phone_number_validation() -> RegexValidator:
    return RegexValidator(
    regex=r"^\+380\d{9}$",
    message="Phone number must be entered in the format: '+380XXXXXXXXX'."
)