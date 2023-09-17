import numpy as np
x = int(input())
n = int(input())


# Return a sequence of numbers counting by `x` `n` times.
def count_by(x=int, n=int):
    array = np.array([x, n], dtype='int')
    return array

count_array = count_by(x, n)
print(count_array)