from hypothesis import given
import hypothesis.strategies as st
## Binary search and Merge sort

def binary_search(ls, target):
    pass

@st.composite
def test_binary_search_element_in_list:
    ls = st.draw(st.lists(elements=st.integers(), min_size = 0, average_size=100).map(sort))
    print(ls)
    i = draw(st.integers(min_value=0, max_value=len(ls) - 1))
    target = ls[i]
    assert binary_search(ls, target) == i
