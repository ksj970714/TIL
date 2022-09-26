#분할 정복

N = int(input())
tree = []
ans = []

for i in range(N):
    tree.append(list(input()))

def quadtree(k, r, c):
    #r부터 c까지, k만큼 for문으로 이동
    #0,1말고 다른게 나오면 쿼드트리를 한번 더 쪼갬
    temp = tree[r][c]
    for i in range(r,k+r):
        for j in range(c,k+c):
            if temp != tree[i][j]:
                ans.append('(')
                halfk = int(k/2)
                quadtree(halfk, r, c)
                quadtree(halfk, r, c+halfk)
                quadtree(halfk, r+halfk, c)
                quadtree(halfk, r+halfk, c+halfk)
                ans.append(')')
                return
            temp = tree[i][j]
    if temp == '0' :
        ans.append('0')
    else:
        ans.append('1')

quadtree(N,0,0)
print(''.join(ans))