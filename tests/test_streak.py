import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_with_zeros_and_negatives():
    """Test with a mix of positive, zero, and negative numbers as per example."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_ones():
    """Test with a streak of ones as per example."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks_longest_is_not_last():
    """Test that the longest streak is correctly identified when it's not the last one."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2]) == 3

def test_streak_at_the_end():
    """Test that a streak at the end of the list is correctly counted."""
    assert longest_positive_streak([-1, 0, 5, 6, 7, 8]) == 4