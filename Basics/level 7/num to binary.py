def nums_to_binary(x):
    binary = ""
    for number in x:
        binary += str(number)
    print(int(binary,2))

    # or
"""
    return int("".join([str(number) for number in x]),2)
"""