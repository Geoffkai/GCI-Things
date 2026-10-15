import numpy as np

def homework(a):
    is_multiple_of_5 = a % 5 == 0

    is_odd = a % 2 == 1

    my_result = a[is_multiple_of_5 & is_odd] 

    return my_result

print(homework(np.array([1, 5, 10, 3, 4, 25, 30])))
print(homework(np.array([2, 4, 6, 8])))