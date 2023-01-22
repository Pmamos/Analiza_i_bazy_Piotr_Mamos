from app import hello
from app import extract_sentiment
from app import text_contain_word
from app import bubble_sort
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata1 = ["I think today will be a great day"]


@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)

    assert sentiment > 0


testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
]


@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):
    assert text_contain_word(word, sample) == expected_output


testdata3 = [
    ([4, 5, 2, 5, 3, 9, 1, 6, 8, 7, 3], [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9])
]


@pytest.mark.parametrize('unsorted, sorted', testdata3)
def test_text_contain_word(unsorted, sorted):
    assert bubble_sort(unsorted) == sorted
