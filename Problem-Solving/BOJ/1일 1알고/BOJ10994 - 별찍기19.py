# 인터넷 그대로 복붙1 (for문 만 사용)

N = int(input())

for i in range(N - 1):
    print("* " * i + "*" * (1 + 4 * (N - i - 1)) + " *" * i)
    print("* " * (i + 1) + " " * (1 + 4 * (N - i - 2)) + " *" * (i + 1))
print("* " * (2 * N - 1))
for i in range(N - 1):
    print("* " * (N - i - 1) + " " * (1 + 4 * i) + " *" * (N - i - 1))
    print("* " * (N - i - 2) + "*" * (1 + 4 * (i + 1)) + " *" * (N - i - 2))

# ===================================================================================
# 인터넷 그대로 복붙2 (재귀함수 사용)

N = int(input())
stars = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]


def fill_star(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        return

    length = 4 * n - 3
    
    for i in range(length):
        stars[y][x + i] = '*'
        stars[y + i][x] = '*'
        stars[y + length - 1][x + i] = '*'
        stars[y + i][x + length - 1] = '*'

    fill_star(n - 1, x + 2, y + 2)


fill_star(N, 0, 0)
for s in stars:
    print(''.join(s))