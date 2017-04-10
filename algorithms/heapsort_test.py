import heapsort
import pytest
from hypothesis import given, reject, settings,  Verbosity
from hypothesis import strategies as st

#Elias' cool way of testing heapsort
#@given(st.lists(st.integers()))
#def test_sorting(ls):
 #   ls = sorted(ls)
  #  for e1, e2 in zip(ls[:-1],ls[1:]):
   #     assert e1 <= e2

@given(ls=st.lists(elements = st.integers(), min_size = 1, average_size = 100, unique = True))
def test_sort_first_element_is_the_smallest(ls):
    ls = heapsort.hs(ls)
    first = ls[0]
    for i in range(1, len(ls)):
        assert first <= ls[i]

@given(ls=st.lists(elements = st.integers(), min_size = 1, average_size = 100, unique = True))
def test_sort_last_element_is_the_largest(ls):
    ls = heapsort.hs(ls)
    last = ls[-1]
    for i in range(0, len(ls)-1):
        assert last >= ls[i]

def test_empty_list():
    ls = []
    assert heapsort.hs(ls) == []

# Tests switch with correct inputs: Inputs a list of elements and two valid indices into the list
@st.composite
def test_switch_list_with_elements_valid_index(draw):
    ls = st.draw(st.lists(elements=st.integers(), min_size = 0, average_size=100, unique=True))
    a = draw(st.integers(min_value=0, max_value=len(ls) - 1))
    b = draw(st.integers(min_value=0, max_value=len(ls) - 1))
    ls_out = heapsort.switch(ls, a, b)
    assert ls_out[a] == ls[b]
    assert ls_out[b] == ls[a]

# Tests that switch correctly throws an index error: Inputs a list of elements and two invalid indices into that list
@st.composite
def test_switch_list_with_elements_invalid_index(draw):
    ls = st.draw(st.lists(elements=st.integers(), min_size = 1, average_size=100, unique=True))
    a = draw(st.integers(min_value=len(ls)))
    b = draw(st.integers(min_value=len(ls)))
    with pytest.raises(IndexError):
        heapsort.switch(ls, a, b)

# Tests switch: Inputs an empty list and two random integers
@given(st.lists(elements=None, max_size=0), st.integers(), st.integers())
def test_switch_empty_list(ls, a, b):
    ls_out = heapsort.switch(ls, a, b)
    assert ls_out == []

# Tests that switch raises a TypeError exception when given insufficient arguments
def test_switch_insufficient_arguments():
    with pytest.raises(TypeError):
        heapsort.switch([1, 2, 3])
