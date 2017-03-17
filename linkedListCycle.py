
def has_cycle(head):
    """
    Detects whether there is a cycle in a linked list.

    Args:
        head: A pointer to the head node of a linkedlist. Contains 'None' if the list is empty.
            A Node is defined as:

                class Node(object):
                    def __init__(self, data = None, next_node = None):
                        self.data = data
                        self.next = next_node
    Returns:
        cycle: A boolean which contains a True if the linkedlist contains a cycle and a False otherwise.
    """

    # We specify that an empty list won't have a cycle.
    if head is None:
        return False

    assert isinstance(head, Node)

    pass

