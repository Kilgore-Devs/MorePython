def array_plus_array(x,y):
    ls = []
    for i in x:
        ls.append(i)
    for i in y:
        ls.append(i)
    return sum(ls)

print(array_plus_array([1, 2, 3], [4, 5, 6]))
print(array_plus_array([-1, -2, -3], [-4, -5, -6]))
print(array_plus_array([0, 0, 0], [4, 5, 6]))
print(array_plus_array([100, 200, 300], [400, 500, 600]))