from django.core.validators import RegexValidator


validate_is_color_string = RegexValidator(
    r"^[#][a-zA-Z0-9]{3,6}$", "Only a Hex formatted string is allowed."
)
