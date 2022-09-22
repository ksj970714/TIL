import sys

sys.setrecursionlimit(10**5) #10**6 으로 나오면 메모리초과나옴.

N = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

ans = []
def divide(l,r,pre):
    if l == r:
        print(inorder[l],end=' ')
        return
    if l > r:
        return
    temp = postorder[r-pre]
    print(temp,end=' ')
    #point = inorder.index(temp)
    for i in range(l,r+1):
        if temp == inorder[i]:
            point = i
    divide(l,point-1,pre)
    divide(point+1,r,pre+1)

divide(0,len(inorder)-1,0)