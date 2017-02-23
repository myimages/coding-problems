# TODO Clean up this and the testing library and then move on.
def hs(Vector):
    """
    Sorts a list of integers using the heapsort algorithm
    PARAMETERS
    Vector - a list of integers
    RETURNS
    VectorSort - the list of integers sorted
    """

    # TODO heapify
    # Builds a max heap in O(n) time.


    Vector = build_max_heap(Vector)

    last = len(Vector) - 1

    #Repeat until the considered range of the list is one element
    while last > 0:
        #Extract the largest number (the root of the heap) and switch it with the number at the last index of the heap. Decrease the considered range of the list by one.
        Vector = switch(Vector, 0, last)
        last = last - 1
        # TODO restore_heap
        #Call the restore_heap() to restore the heap within the confines of the new considered range
        Vector = restore_heap(Vector, 0, last)

    return Vector

def switch(Vector, Index1, Index2):
    """
    Takes a list and switches the two elements at Index1 and Index2
    """
    if Vector == []:
        return(Vector)
    try:
        tmp = Vector[Index1]
        Vector[Index1] = Vector[Index2]
        Vector[Index2] = tmp
        return Vector
    except IndexError:
        return Vector


# Rough version
def build_max_heap(Vector):
    Latest = len(Vector) - 1

    while Latest >= 0:
        Vector = restore_heap(Vector, Latest, len(Vector) - 1)
        Latest = Latest - 1
    return Vector

def restore_heap(Vector, Latest, Fin):
    # TODO
    # Implement sift down heap function
    Root = Latest

    while left_child_of(Root) <= Fin:
        LeftChild = left_child_of(Root)
        Largest = Root
        if Vector[Largest] < Vector[LeftChild]:
            Largest = LeftChild
        if right_child_of(Root) <= Fin and Vector[Largest] < Vector[right_child_of(Root)]:
            Largest = right_child_of(Root)
        if Largest == Root:
            return Vector
        else:
            Vector = switch(Vector, Root, Largest)
            Root = Largest
    return Vector

def parent_of(Childi):
    # The children of parent i are located at 2i and 2i + 1
    if Childi % 2 == 1:
        return Childi - 1 / 2
    else:
        return Childi / 2


def right_child_of(Parenti):
    return Parenti * 2 + 1

def left_child_of(Parenti):
    # The left child of parent i is at index 2i
    return Parenti * 2
