import pytest
import hypothesis

class Node(object):
    """
    Node object which is being used to test the functions.

    Delete before submitting.

     Args:
        data (:anything): Data which is contained in the LinkedList node.
        next_node (:obj type Node): Pointer to the subsequent node in the linkedList.

    Attributes:
        data (:anything): Data which is contained in the LinkedList node.
        next_node (:obj type Node): Pointer to the subsequent node in the linkedList.

    """
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

    def set_next(self, new_next):
        self.next_node = new_next

    def insert(self, data):
        new_node = Node(data)
        self.set_next(new_node)

######################################################################

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
        head.insert(ls[1])
        node = head.next
        for i in range(2, len(ls)):
            node.insert(ls[i])
            node = node.next
    return head

def print_linked_list(node):
    """
        Prints a linked list

    Args:
        node (:obj Node): The head node of the linked list.
    """
    while node is not None:
        print("Node: " + str(node.data) + "; ")
        node = node.next

######################3

def test_tests():
    pass
