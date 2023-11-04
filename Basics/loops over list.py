# for i in range(low, high):
#     print(i)
#
# for i in range(len(lst)):
#     print(lst[i])
#
# for element in lst:
#     print(element)
#
# for i, element in enumerate(lst):
#     print(i)
sum_ = 0
for i in range(0, 30):  # find sum of nums in the range of 0-29
    sum_ += i
print(sum_)
#or
print(sum(range(30)))
# sum range in inc of 3
sum_ = 0
for i in range(0, 30, 3):  # find sum of nums in the range of 0-29
    sum_ += i
print(sum_)
#appending values
sum_ = 0
nums = []
for i in range(0, 30, 3):  # find sum of nums in the range of 0-29
    nums.append(i)
    sum_ += i
print(sum_)
print(nums)


for i in range(len(nums)):
    print(f' + {nums[i]} ')
print(f' = {sum_}')

st = ''
for x in range(len(nums)):  # how to acces the values/integers in a list
    st += str(nums[x]) + ' + '  # to add a int to a string use str()
print(f'{st} = {sum_}')


lst = list(range(10))
print(lst)
# remove numbers that are divisbel by 3
# but it doesnt work properly, remoove the item and shifts itmes to left and keeps iteraing thus skipping values
# for n in lst:
#     if n % 3 == 0:
#         lst.remove(n)
#     else:
#         print(n)
# print(f'{lst=}')

# works correclty
for n in reversed(lst):  #or for n in list(lst)
    if n % 3 == 0:
        lst.remove(n)
    else:
        print(n)
print(f'{lst=}')

number = 3
ls_num = [1,2,3,4,5,6,7,8,9,10]
if(number in ls_num):
    print("3 is in the list")
else:
    print("not in the list")

#yset = {'a',1, 'b',2, 'c',3}    #set not a dict

xdict = {'x':1, 'b':2, 'c':3}   #dict

print(xdict)
print(xdict['c']) #print the value of key 'c'
xdict['c']= 10 #change key, will add the k:v if not in dict
print(xdict) # print changed dict
coolcap = xdict['c'] #reading value for c. so value for coolcap will be the value of c
print(coolcap)
#myset.add(newitem) adds newitem to set
# len(), loop with for, in membership
#sorted() min() max() sum()
# when working with the about, you are working with the KEY not th evalue
print(len(xdict)) # print the number of k:v pairs
print(sorted(xdict))
for item in xdict:  # item is key unless ' for key, value in dict:
    print(item)     # print(key, value) or can try whats below
for key, in xdict:
    print(key, '=', xdict[key])

for key in xdict:
    value = xdict[key]
    print(key, value)
#dict methods
# .keys()  .values()  .items()  .get()
print(xdict.keys())
print(xdict.values())
print(xdict.items()) # returns list of tuples with the k:v bein inside a tuple
for value in xdict.values():
    print(value)
# if you want a list of items, set a var to a list
x = list(xdict.values())
y = list(xdict.items())
print(x)
print(y)
huh = xdict.get('c')  # get a value based on key
print(huh)

userkey = input('enter a key:  ')
value = xdict.get(userkey, 100) # set 100 as default value if key isn't in dict can set as None
if userkey not in xdict:
    print("Not found")
else:
    print(xdict[userkey])
# form  dict from a file
empty_dict = {}
somefile = open('filename')
for line in somefile:
    country, state, city = line.split(',') # splits the line into three columns separated by a ','. coutnry, state, city
    # setup key value pair
    empty_dict[country] = state  # key will be coutnry, value will be state use .rstip() to remove \n etc

# how to aggrregate
# if you want to find out how many times a state is in the dict
# {OH: 3, NY: 2, FL: 7} for exampple
    # take the value for state, add one to it
    #assign that new value to the dict for this key
    if state not in empty_dict:  # check if key of stat is in the did
        empty_dict[state] = 0  # adds the key if its not
    empty_dict[state] = empty_dict[state] + 1 # running count of everytime a state is in the dict


"""
dictionaries. key:value pairs.
"""
student  = {'name':'jon', 'age':25, 'courses':['math', 'compsci', 'history']}

print(student['courses'])
print(student.get('name'))
print(student.get('grade', 'Not Found')) # shows not found because its not in dict
#addnew entry
student['grade'] = 'A' # adds k:v grade:A
print(student.get('grade', 'Not Found')) # print new entry
student.update({'name': 'brandon', 'age': 30}) # updates
print(student)
# delete key
del student['age']
# or
name = student.pop('name') # removes key but adds to variable
print(name)
print(student)
#loop through
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, value)



