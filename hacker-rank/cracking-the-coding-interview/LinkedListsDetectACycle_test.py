"""
Test suite for 04LinkedListsDetectACycle.py
"""

# TODO: Once I figure out which modules I will use, replace the import statements with from statements.
import LinkedListsDetectACycle as lldal
from LinkedListsDetectACycle import Node
import pytest
import hypothesis
from unittest import mock

# Constructs a linked list from a list of data
def make_linked_list(ls):
    if not ls:
        head = Node(data=None)
        return head


    for data in ls:


# Specification: An empty list does not contain a cycle.
def test_empty_list():
    assert linkedListCycle.has_cycle(head=None) == False

# Test that if the input is not a Node or None, the program does not run.
def test_incorrect_input():
        with pytest.raises(AssertionError):
            linkedListCycle.has_cycle(head=1)

def test_one_element():

    assert linkedListCycle.has_cycle(head=head)


