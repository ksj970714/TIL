a = input()
b = input()

mydp = []

temp = [""]*(len(b)+1)
for i in range(len(a)+1):
    mydp.append(temp[:])

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            mydp[i][j] = mydp[i-1][j-1] + a[i-1]
        else:
            if len(mydp[i-1][j]) > len(mydp[i][j-1]):
                mydp[i][j] = mydp[i-1][j]
            else:
                mydp[i][j] = mydp[i][j-1]
print(len(mydp[-1][-1]))
print(mydp[-1][-1])



