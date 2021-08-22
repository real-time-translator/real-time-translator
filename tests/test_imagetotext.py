import pytest
from real_time_translator.imagetotext import imagetotext

def test_image_to_text_string_translate():
    actual=imagetotext('assests/imagetotext/img2.jpg')
    expected='مرحبا بالعالم!'
    assert actual==expected