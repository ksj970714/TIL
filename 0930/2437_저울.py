N = int(input())
mylist = sorted(list(map(int,input().split())))

hap = 0
for i in range(N):
    if hap + 1 < mylist[i]:
        break
    else:
        hap += mylist[i]
print(hap+1)