"""
Test suite for linkedListCycle.py
"""

# TODO: Once I figure out which modules I will use, replace the import statements with from statements.
import linkedListCycle
import pytest
import hypothesis

# Specification: An empty list does not contain a cycle.
def test_empty_list():
    assert linkedListCycle.has_cycle(head=None) == False

# I will need to create a mock node object. : )
