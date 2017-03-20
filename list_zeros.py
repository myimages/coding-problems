"""
You have a list and you want to push all of the zeros to the end
Learning about TDD
"""

def push_zeros(ls):
    if len(ls) > 1:
        ls_latter = push_zeros(ls[1:])
        ls_former = [ls[0]]
        if ls[0] == 0:
            return ls_latter + ls_former
        else:
            return ls_former + ls_latter
    return ls

