import pytest
from real_time_translator.imagetotext import imagetotext

def test_image_to_text_string_translate():
    actual=imagetotext('assests/imagetotext/img2.jpg')
    expected='Hello World!\n\x0c'
    assert actual==expected