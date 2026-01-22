import pytest
import sys
sys.path.append('..')

from palindrome import longest_palindromic_substring

@pytest.mark.parametrize("input, expected", [
    ("babad", "bab"),  # or "aba"
    ("cbbd", "bb"),
    ("a", "a"),
    ("ac", "a" or "c"),  # or "c"
    ("", ""),
    ("racecar", "racecar"),
    ("noon", "noon"),
])

def test_longest_palindromic_substring(input, expected):
    result = longest_palindromic_substring(input)
    assert result == expected or result == expected[::-1]  # account for multiple valid outputs