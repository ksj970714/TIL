a = []
import math
def euclid(x,y):
    if y == 0 :
        a.append(x)
        return
    temp = y
    y = x % y
    x = temp
    euclid(x,y)
x, y = map(int,input().split())
if x < y:
    x,y = y,x

euclid(x,y)
print(a[0])
print(int(x*y/a[0]))