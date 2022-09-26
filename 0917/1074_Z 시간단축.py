z_search = [[0, 0], [0, 1], [1, 0], [1, 1]]
global count
count = 0


def z(n, r, c):
    global count

    # n == 1일때 한 점을 찍고 이동
    if n == 1:
        for search in z_search:
            if x == r + search[0] and y == c + search[1]:
                print(count)
                break
            else:
                count += 1
        return

    if x < r + (2 ** (n - 1)) and y < c + (2 ** (n - 1)):
        z(n - 1, r + (2 ** (n - 1)) * (z_search[0][0]), c + (2 ** (n - 1)) * (z_search[0][1]))
    else:
        count += (2 ** (n - 1)) ** 2

    if x < r + (2 ** (n - 1)) and y >= c + (2 ** (n - 1)):
        z(n - 1, r + (2 ** (n - 1)) * (z_search[1][0]), c + (2 ** (n - 1)) * (z_search[1][1]))
    else:
        count += (2 ** (n - 1)) ** 2

    if x >= r + (2 ** (n - 1)) and y < c + (2 ** (n - 1)):
        z(n - 1, r + (2 ** (n - 1)) * (z_search[2][0]), c + (2 ** (n - 1)) * (z_search[2][1]))
    else:
        count += (2 ** (n - 1)) ** 2

    if x >= r + (2 ** (n - 1)) and y >= c + (2 ** (n - 1)):
        z(n - 1, r + (2 ** (n - 1)) * (z_search[3][0]), c + (2 ** (n - 1)) * (z_search[3][1]))


n, x, y = map(int, input().split())

z(n, 0, 0)
