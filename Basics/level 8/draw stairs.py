def draw_stairs(n):
    stairs = ""
    for i in range(n):
        stairs += " " * i + "I\n"
    return stairs[:-1]
"""    also works
def draw_stairs(n):
    ans="I"
    for i in range(1,n):
        ans+="\n"+i*" "+ "I"
        
    return ans
"""
print(draw_stairs(3))#, '''I\n I\n  I''')
print(draw_stairs(5))#, '''I\n I\n  I\n   I\n    I''')