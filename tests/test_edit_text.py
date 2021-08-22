from unittest import mock
from unittest.mock import patch

from real_time_translator.edit_text import edit_text

def test_edit_text():
    old_text = "Hi"
    with mock.patch('builtins.input', return_value=f"{old_text}Hello!"):
        edited_text = edit_text("", old_text)
        assert edited_text == 'HiHello!'
