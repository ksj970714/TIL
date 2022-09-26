#분할 정복
#재귀 활용: 1 2 3 4 순으로 탐색하는 함수
# n = 1인 시점에 오른쪽으로 집어넣음

#집어넣을 필요 없이 해당지점이 되면 반환한다.
#z는 뭐하는 함수여야 하는가?
#n=1일땐 num을 z_search 순서대로 집어넣는 함수. num+= 1, r,c가 되면 리턴
#이외일 땐 더할필요 없으니? 4만 더해주고 리턴, ㅠㅍ 불필요한 연산을 하지 않음.
#n>2일땐 분할하는 함수
z_search = [[0,0],[0,1],[1,0],[1,1]]
global count
count = 0


def z(n,r,c):
    global count

    # n == 1일때 한 점을 찍고 이동
    if n == 1:
        for search in z_search:
            if x == r+search[0] and y == c+search[1]:
                print(count)
                break
            else:
                count += 1
        return
    
    z(n-1,r+(2**(n-1))*(z_search[0][0]),c+(2**(n-1))*(z_search[0][1]))
    z(n-1,r+(2**(n-1))*(z_search[1][0]),c+(2**(n-1))*(z_search[1][1]))
    z(n-1,r+(2**(n-1))*(z_search[2][0]),c+(2**(n-1))*(z_search[2][1]))
    z(n-1,r+(2**(n-1))*(z_search[3][0]),c+(2**(n-1))*(z_search[3][1]))

n,x,y = map(int,input().split())

z(n,0,0)
