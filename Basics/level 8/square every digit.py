def square_digits(num):
    nums = str(num)
    ans = ''

    for i in nums:
        x = int(i) * int(i)
        ans += str(x)
    return int(ans)


print(square_digits(9119))  # returns 811181