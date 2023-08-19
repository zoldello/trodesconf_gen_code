import pytest

import trode_config_generator


@pytest.mark.parametrize(
    "question, expected",
    (
        ("What's the meaning of life?", "42"),
        ("Are you serious?", "42"),
        ("How old are you?", "42"),
        ("", "42"),
        ("This is not a question!", "42"),
    )
)
def test_deep_thought(question, expected):
    assert trode_config_generator.DeepThought.get_answer(question) == expected
