"""
Anja and Adriel's solution to: https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight

WIP - Not finished or optimised
"""

def num_parse(n, N):
    i = 0
    input_digits = []
    for i in range(0, n, 1):
        input_digits.append(int(str(N)[i]))
    return(input_digits)

def combiner(input_digits):
    permutations = []
    for i, n in enumerate(input_digits):
        permutations.append(n)
        for j, o in enumerate(input_digits):
            if i < j:
                permutations.append(n*10 + o)
            for k, p in enumerate(input_digits):
                if i < j < k:
                    permutations.append(n*100 + o*10 + p*1)
    return permutations

def divisible_by_eight(permutation_array):
    div_by_eight = []
    mult_of_eight = [i for i in range(0, 1000, 8)]
    for number in permutation_array:
        if number in mult_of_eight:
            div_by_eight.append(number)
    return div_by_eight

def more_divisible_by_eight(div_by_eight, input_digits):
    str_input_digits = ''.join(map(str, input_digits))
    str_div_by_eight = list(map(str, div_by_eight))
    for i, n in enumerate(str_div_by_eight):
        if len(n) == 3:
            print(n)
    return str_div_by_eight

# Set Upper
input_digits = num_parse(4, 5968)
permutations = combiner(input_digits)
# Remove duplicates
permutations = list(set(permutations))

div_by_eight = divisible_by_eight(permutations)
div_by_eight = more_divisible_by_eight(div_by_eight, input_digits)
print(div_by_eight)
