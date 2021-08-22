import pytest
from real_time_translator.voice import *

def test_trascript():
   file = "source/test_file.wav"
   actual = transcript_from_file(file)
   expected = 'hello everyone'
   assert actual == expected