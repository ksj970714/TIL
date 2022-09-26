import math
N = int(input())
a='  *  '
b=' * * '
c='*****'
myprint = [a,b,c]

#출력 후 myprint에 추가
for _ in range(int(math.log2(N//3))):

    new = []
    curlen= len(myprint)
    for i in range(curlen):
        new.append(' '*(curlen*2-1-i)+myprint[i].strip()+' '*(curlen*2-1-i))
    for i in range(curlen):
        new.append(' ' * (curlen-1-i) + (myprint[i]+' '+myprint[i]).strip()+' ' * (curlen-1-i) )
    myprint = new
for i in myprint:
    print(i)