myCircle = []
myRadius = [1,2,3,4,5,6,7,8,9,10]

def circle(radius):
    c = 2*3.15*radius
    return c

for r in myRadius:
    myCircle.append(int(circle(r)))

print(myCircle)
