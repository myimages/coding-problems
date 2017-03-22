"""
Test suite for 04LinkedListsDetectACycle.py
"""

# TODO: Once I figure out which modules I will use, replace the import statements with from statements.
from LinkedListsDetectACycle import Node, has_cycle
import pytest
import hypothesis

# Constructs a linked list from a list of data
def make_linked_list(ls):
    """
    Constructs a linked list out of a list of data.

    Args:
        ls (:list): A list whose values will be converted into a linked list of Node objects. If there are duplicate values in the list, it is assumed they are referring to the same Node.

    Returns:
        head (:obj Node): The head node of the linked list.
    """
    if not ls:
        head = Node(data=None)
    elif len(ls) == 1:
        head = Node(data=ls[0])
    else:
        head = Node(data=ls[0])
        head.set_next(Node(ls[1]))
        node = head.next
        for i in range(2, len(ls)):
            node.set_next(Node(ls[i]))
            node = node.next
    return head

def print_linked_list(node):
    """
        Prints a linked list

    Args:
        node (:obj Node): The head node of the linked list.
    """
    ll = ""
    while node is not None:
        ll += "Node: " + str(node.data) + "; "
        node = node.next
    return ll


# Specification: An empty list does not contain a cycle.
def test_empty_list():
    assert has_cycle(head=None) == False

# Test that if the input is not a Node or None, the program does not run.
def test_incorrect_input():
        with pytest.raises(AssertionError):
            has_cycle(head=1)

def test_one_element():

    assert has_cycle(head=head)

def test_make_linked_list():
    assert print_linked_list(make_linked_list([1])) == "Node: 1; "
    assert print_linked_list(make_linked_list([1, 2])) == "Node: 1; Node: 2; "
    assert print_linked_list(make_linked_list(["1", "2", "3"])) == "Node: 1; Node: 2; Node: 3; "

def test_print_linked_list():
    head = Node(data=1)
    head.set_next(Node(data=2))
    head.next.set_next(Node(data=3))
    assert print_linked_list(head) == "Node: 1; Node: 2; Node: 3; "

