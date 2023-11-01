"""
A number is Esthetic if, in any base from base2 up to base10, the absolute difference between every pair of its adjacent digits is constantly equal to 1.

num = 441 (base10)
// Adjacent pairs of digits:
// |4, 4|, |4, 1|
// The absolute difference is not constant
// 441 is not Esthetic in base10

441 in base4 = 12321
// Adjacent pairs of digits:
// |1, 2|, |2, 3|, |3, 2|, |2, 1|
// The absolute difference is constant and is equal to 1
// 441 is Esthetic in base4
Given a positive integer num, implement a function that returns an array containing the bases (as integers from 2 up to 10) in which num results to be Esthetic, or an empty array [] if no base makes num Esthetic.

Examples
10 ➞ [2, 3, 8, 10]
// 10 in base2 = 1010
// 10 in base3 = 101
// 10 in base8 = 12
// 10 in base10 = 10

23 ➞ [3, 5, 7, 10]
// 23 in base3 = 212
// 23 in base5 = 43
// 23 in base7 = 32
// 23 in base10 = 23

666 ➞ [8]
// 666 in base8 = 1232
"""
def esthetic(x):

    ans = []  # empty list to store the bases in which x is Esthetic.

    for base in range(2, 11):  # Loop through bases from 2 to 10.
        numbers = []  # empty list to store the digits of x in the current base.
        n = x  # Create a copy of x to avoid modifying the original number.
        while n > 0:  # While statemet to convert x to the current base and extract its digits.
            numbers.append(n % base)  # Append the rightmost digit to the list.
            n //= base  # Remove the rightmost digit.
        numbers = numbers[::-1]  # Reverse the list to get the digits in their original order.
        is_esthetic = True  # check if x is Esthetic in the current base.

        for i in range(1, len(numbers)):  # Iterate through the digits and check the absolute difference between adjacent digits.
            if abs(numbers[i] - numbers[i - 1]) != 1:
                is_esthetic = False# If the absolute difference is not 1, set the flag to False and exit the loop.
                break
        if is_esthetic:  # If is_esthetic is still True, x is Esthetic in the current base, so add the base to the list.
            ans.append(base)
    return ans


print(esthetic(10))#, [2, 3, 8, 10], "Example #1")
print(esthetic(23))#, [3, 5, 7, 10], "Example #2")
print(esthetic(666))#, [8], "Example #3")
print(esthetic(13))#, [5, 6])
print(esthetic(1))#, [2, 3, 4, 5, 6, 7, 8, 9, 10])
print(esthetic(9))#, [4, 7, 9, 10])
print(esthetic(74))#, [])
print(esthetic(740))#, [4, 6, 9])
print(esthetic(928))#, [])
print(esthetic(259259))#, [9])
print(esthetic(883271))#, [])
print(esthetic(1080898))#, [7])
print(esthetic(1080899))#, [])