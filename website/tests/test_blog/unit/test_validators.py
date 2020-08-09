import pytest
from django.core.exceptions import ValidationError
from blog.validators import validate_is_color_string


@pytest.mark.parametrize("color, expected_result", [("#222", True), ("222", False)])
def test_tag_background_validator(color, expected_result):
    try:
        validate_is_color_string(color)
        assert expected_result
    except ValidationError:
        assert expected_result is False
