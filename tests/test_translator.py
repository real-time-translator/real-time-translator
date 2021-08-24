import pytest
from real_time_translator.translator import translat_str


def test_translate_single_word():
 word="تفاحة"
 actual=translat_str(word,'en').lower()
 expected='تفاحة (ar) --> apple (en)'
 assert actual == expected



def test_translate_single_santance():
 word="اكلت تفاحة"
 actual=translat_str(word,'en').lower()
 expected='اكلت تفاحة (ar) --> i ate an apple (en)'
 assert actual == expected