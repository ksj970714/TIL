a = input()
b = input()

mydp = []

temp = [0]*(len(b)+1)
for i in range(len(a)+1):
    mydp.append(temp[:])

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            mydp[i][j] = mydp[i-1][j-1] + 1
        else:
            mydp[i][j] = max(mydp[i-1][j],mydp[i][j-1])

print(mydp[-1][-1])