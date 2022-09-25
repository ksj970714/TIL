import sys
import collections
N = int(input())
mydict = collections.defaultdict(list)

for i in range(N):
    word = sys.stdin.readline().rstrip()
    mydict[len(word)].append(word)

for i in range(51):
    for word in sorted(list(set(mydict[i]))):
        print(word)

