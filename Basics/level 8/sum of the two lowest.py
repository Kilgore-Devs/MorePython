def sum_two_smallest_numbers(x):
    x = sorted(x)
    ans = int(x[0]) + int(x[1])
    return x.sort()

# ORRRR
"""
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))
