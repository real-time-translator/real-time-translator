from unittest import mock
from unittest.mock import patch

from real_time_translator.input_text_manually import input_text_manually , input_text_file

def test_input_text_manually():
    with mock.patch('builtins.input', return_value="Hello!"):
        actual = input_text_manually()
        assert actual == "Hello!"
        assert type(actual) == str

def test_input_text_file():
    with mock.patch('builtins.input', return_value="input_text/input.txt"):
        actual = input_text_file()
        assert actual == "hello my name is yahia."
        assert type(actual) == str
    # with mock.patch('builtins.input', return_value="/home/nura/Documents/test"):
    #     actual = input_text_file()
    #     assert actual == "hello yahia\n"
    #     assert type(actual) == str


   