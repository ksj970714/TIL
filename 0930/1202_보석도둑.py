import sys
import heapq

N, K = map(int,input().split())
bosuk = []
for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    bosuk.append([b, a])
gabang = []
for i in range(K):
    gabang.append(int(sys.stdin.readline()))



heapq.heapify(bosuk)
length = len(bosuk)
for i in range(length):
