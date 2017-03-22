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
        self.next = new_next



def has_cycle(head):
    """
    Detects whether there is a cycle in a linked list.

    Args:
        head (:obj type Node): A pointer to the head Node of a linkedlist. Contains 'None' if the list is empty.
            A Node is defined as:

                class Node(object):
                    def __init__(self, data = None, next_node = None):
                        self.data = data
                        self.next = next_node
    Returns:
        cycle (:boolean): Contains a True if the linkedlist contains a cycle and a False otherwise.
    """

    # We specify that an empty list won't have a cycle.
    if head is None:
        return False

    assert isinstance(head, Node)

    pass

