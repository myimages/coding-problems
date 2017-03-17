"""
Test suite for linkedListCycle.py
"""

# TODO: Once I figure out which modules I will use, replace the import statements with from statements.
import linkedListCycle
import pytest
import hypothesis
from unittest import mock

# Specification: An empty list does not contain a cycle.
def test_empty_list():
    assert linkedListCycle.has_cycle(head=None) == False

# Test that if the input is not a Node or None, the program does not run.
def test_incorrect_input():
        with pytest.raises(AssertionError):
            linkedListCycle.has_cycle(head=1)

# Mock objects : D

