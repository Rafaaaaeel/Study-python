x = float(input('x: '))
y = float(input('y: '))
p = 0

#plan_range_x = [1,2,3,4,5]
#plan_range_y = [1,2,3,4,5]

def plan_square (x,y):
    if x < 0 and y >= 0:
        p = 2
    elif x > 0 and y < 0:
        p = 4
    elif x > 0 and y > 0:
        p = 1
    else:
        p = 3
    
    return p

value = plan_square(x,y)
print(f"Square position: {value}")