import pytest
from django.core.exceptions import ValidationError
from blog.validators import validate_is_color_string


@pytest.mark.parametrize("correct, incorrect", [("#222", "222")])
def test_tag_background_validator(correct, incorrect):
    validate_is_color_string(correct)
    with pytest.raises(ValidationError):
        validate_is_color_string(incorrect)
