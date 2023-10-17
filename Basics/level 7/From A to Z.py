"""
Given a string indicating a range of letters, return a string which includes all the letters in that range,
including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

Examples
"a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
"h-o" ➞ "hijklmno"
"Q-Z" ➞ "QRSTUVWXYZ"
"J-J" ➞ "J"
Notes
A hyphen will separate the two letters in the string.
You don't need to worry about error handling in this one
(i.e. both letters will be the same case and the second letter will always be after the first alphabetically).
"""


def gimme_the_letters(x):
    ans = []
    for q in range(ord(x[0]), ord(x[2])+1, 1):
        ans.append(chr(q))
#    newl = ''.join(x)  # create a new list based off old list
    return ''.join(ans)


print(gimme_the_letters("a-z"))  # "abcdefghijklmnopqrstuvwxyz"
print(gimme_the_letters("h-o"))  # "hijklmno"
print(gimme_the_letters("Q-Z"))  # "QRSTUVWXYZ"
print(gimme_the_letters("J-J"))  # "J"
print(gimme_the_letters("a-b"))  # "ab"
print(gimme_the_letters("A-A"))  # "A"
print(gimme_the_letters("g-i"))  # "ghi"
print(gimme_the_letters("H-I"))  # "HI"
print(gimme_the_letters("y-z"))  # "yz"
print(gimme_the_letters("e-k"))  # "efghijk"
print(gimme_the_letters("a-q"))  # "abcdefghijklmnopq"
print(gimme_the_letters("F-0"))  # "FGHIJKLMNO"
