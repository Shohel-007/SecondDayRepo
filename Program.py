<<<<<<< Updated upstream
//This Code is the HomePage of the Application developed by Dev1

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

# Reverse first d elements
arr[:d] = reversed(arr[:d])

# Reverse remaining elements
arr[d:] = reversed(arr[d:])

# Reverse entire array
arr.reverse()
print(arr)
=======
// This is the Cart Interface code developed by dev2

import math

def is_perfect_sq(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_sq(5 * n * n + 4) or is_perfect_sq(5 * n * n - 4)

for i in range(1, 7):
    if is_fibonacci(i):
        print(f"{i} is a Fibonacci Number")
    else:
        print(f"{i} is not a Fibonacci Number")

>>>>>>> Stashed changes
