"""
Write a function that receives an integer n and produces the representing set.

Examples
rep_set(0) ➞ []

rep_set(1) ➞ [[]]

rep_set(2) ➞ [[], [[]]]

rep_set(3) ➞ [[], [[]], [[], [[ ]]]]

"""
def empty(x):
    if x == 0:
        return []
    elif x == 1:
        return [[]]
    else:
        ans = empty(x - 1)

    return ans + [ans]

print(empty(0))  # []
print(empty(1))  # [[]]
print(empty(2))  # [[], [[]]]
print(empty(3))  # [[], [[]], [[], [[ ]]]]
print(empty(5))  #[[], [[]], [[], [[]]], [[], [[]], [[], [[]]]], [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]]]])



