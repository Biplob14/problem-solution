import cmath

x1, y1, x2, y2 = input().split()

print(x1)
print(y1)
print(x2)
print(y2)
x = int(x2) - int(x1)
y = int(y2) - int(y1)
distance = cmath.sqrt( x**2 + y**2 )
print("x: ", distance)