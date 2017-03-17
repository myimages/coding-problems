"""
Test suite for linkedListCycle.py
"""

# TODO: Once I figure out which modules I will use, replace the import statements with from statements.
import linkedListCycle
import pytest
import hypothesis
from unittest import mock

# Class Node for testing
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
    def set_next(self, new_next):
        self.next_node = new_next
    def insert(self, data):
        new_node = Node(data)
        self.set_next(new_node)

# Specification: An empty list does not contain a cycle.
def test_empty_list():
    assert linkedListCycle.has_cycle(head=None) == False

# I will need to create a mock node object. : )
