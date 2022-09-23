from collections import defaultdict

N = int(input())


def binarysearch(temp, l, r,i):
    print(l,r,myans)
    if r - l == 1:
        myans[r] = temp
        mydict[r].append([i + 1, temp])
        return

    mid = (l + r) // 2
    if temp <= myans[mid]:
        binarysearch(temp, l, mid, i)
    else:
        binarysearch(temp, mid, r, i)

mylist = list(map(int, input().split()))
mylist.append(0)
myans = [float('-inf')]
mydict = defaultdict(list)
myanslen = 1
# currentlen 현재길이
# myans len이 n인 시점에 가장 최소의 숫자가 들어간 것
for i in range(len(mylist) - 1):
    temp = mylist[i]

    if myans[-1] < temp:
        myans.append(temp)
        myanslen += 1
        mydict[myanslen - 1].append([i + 1, temp])
    else:
        binarysearch(temp,0,myanslen,i)


print(myanslen - 1,myans)
p, q = sorted(mydict[myanslen-1],reverse=True)[-1][0], sorted(mydict[myanslen-1],reverse=True)[-1][1]
suyeol = [q]
for i in range(myanslen-2,0,-1):
    for j in range(len(mydict[i])):
        if mydict[i][j][0] < p and mydict[i][j][1] < q:
            p, q = mydict[i][j][0],mydict[i][j][1]
            suyeol.append(q)
            break
print(*reversed(suyeol))