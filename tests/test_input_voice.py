import pytest
from real_time_translator.input_voice import *

def test_trascript():
   file = "assets/voices/test_file.wav"
   actual = transcript_from_file(file)
   expected = 'hello everyone'
   assert actual == expected