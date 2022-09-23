import math
N = int(input())
a='  *   '
b=' * *  '
c='***** '
myprint = [a,b,c]

#출력 후 myprint에 추가
for _ in range(int(math.log2(N))):
    for i in myprint:
        print(i)
    new = []
    curlen= len(myprint)
    for i in range(curlen):
        new.append(myprint[i])
    for i in range(curlen):
        new.append(' ' * (curlen-1-i) + (myprint[i]*2))
    myprint = new
