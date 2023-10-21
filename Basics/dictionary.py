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


