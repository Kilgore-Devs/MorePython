"""
Create a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number.

Worked Example
2520 ➞ 72

# The first and last digits are 2 and 0.
# 2 and 0 form 20.
# The second digit is 5 and the second to last digit is 2.
# 5 and 2 form 52.

# 20 + 52 = 72
Examples
121 ➞ 13
# 11 + 2

1039 ➞ 22
# 19 + 3

22225555 ➞ 100
# 25 + 25 + 25 + 25
Notes
If the number has an odd number of digits, simply add on the single-digit number in the center (see example #1).
Any number which is zero-padded counts as a single digit (see example #2).
"""

def closing_in_sum(x):
    a = []  # WWKD...Create an empty list.

    stnum = str(x)  # Convert the input integer 'x' to a string and store it in 'stnum'.
    lsnum = list(stnum)  # Create a list 'lsnum' by converting the string 'stnum' to a list of characters.

    for i in stnum:  # Iterate over each character in the string 'stnum'.

        while len(lsnum) > 1:
            a += [lsnum[0] + lsnum[-1]]   # Enter a while loop as long as 'lsnum' has more than one character.
            del lsnum[0]  # Remove the first and last characters from 'lsnum'.
            del lsnum[-1]

        if len(lsnum) == 1:  # If 'lsnum' has only one character left, append it to list 'a'.
            a.append(lsnum[0])

        return sum([int(num) for num in a])  # Calculate the sum of all elements in 'a' after converting them to integers.
                                             # and return this sum as the result of the function
# why do i suck at this :(




print(closing_in_sum(121))#, 13)
print(closing_in_sum(10390))#, 22)
print(closing_in_sum(22225555))#, 100)
print(closing_in_sum(2520))# 72)
print(closing_in_sum(5332824166496569))#, 331)
print(closing_in_sum(1979672314137318116))#, 485)
print(closing_in_sum(1795459644013947776))#, 548)
print(closing_in_sum(2801980378842185820))#, 426)
print(closing_in_sum(3440584288422776554))#, 430)
print(closing_in_sum(1985124000275401986))#, 342)
