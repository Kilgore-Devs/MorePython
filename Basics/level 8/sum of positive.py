def positive_sum(x):
    ans = 0
    for i in x:
        if i > 0:
            ans += i

    return ans

"""
orrrr
return sum(i for i in x if x >0)"""



print(positive_sum([1,2,3,4,5]))
print(positive_sum([1,-2,3,4,5]))
print(positive_sum([-1,2,3,4,-5]))

