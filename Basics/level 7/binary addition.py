def add_binary(a,b): return (bin(a + b)[2:])
"""this works too"""
    # tot = a + b
    # lst = []
    # while tot > 0:
    #     dig = tot % 2
    #     lst.append(dig)
    #     tot = tot // 2
    # lst.reverse()
    # st = []
    # for i in lst:
    #     i = str(i)
    #     st.append(i)
    # ans = "".join(st)
    # return ans

print(add_binary(1, 1))#, "10")
print(add_binary(0, 1))#, "1")
print(add_binary(1, 0))#, "1")
print(add_binary(2, 2))#, "100")
print(add_binary(51, 12))#, "111111")