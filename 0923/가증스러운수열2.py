from collections import defaultdict

N = int(input())


def binarysearch(temp, l, r):
    print(l,r,myans)
    if r - l == 1:
        myans[r] = temp
        return

    mid = (l + r) // 2
    if temp <= myans[mid]:
        binarysearch(temp, l, mid)
    else:
        binarysearch(temp, mid, r)

mylist = list(map(int, input().split()))
mylist.append(0)
myans = [float('-inf')]
myanslen = 1
# currentlen 현재길이
# myans len이 n인 시점에 가장 최소의 숫자가 들어간 것
for i in range(len(mylist) - 1):
    temp = mylist[i]

    if myans[-1] < temp:
        myans.append(temp)
        myanslen += 1
    else:
        binarysearch(temp,0,myanslen)


print(myanslen - 1,myans)