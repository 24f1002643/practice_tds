import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_with_zero():
    """Test that zero breaks the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negative():
    """Test that a negative number breaks the streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4]) == 2

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 6]) == 4

def test_streak_at_beginning():
    """Test when the longest streak is at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 4, -1, 5, 6]) == 4