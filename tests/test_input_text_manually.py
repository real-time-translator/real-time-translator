from unittest import mock
from unittest.mock import patch

from real_time_translator.input_text_manually import input_text_manually

def test_input_text_manually():
    with mock.patch('builtins.input', return_value="Hello!"):
        actual = input_text_manually()
        assert actual == "Hello!"
        assert type(actual) == str