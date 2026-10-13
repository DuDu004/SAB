n, X = map(int, input().split())
inset = list(map(int, input().split()))
table = [[False] * (X + 1) for _ in range(n + 1)]

def subsum(table):
    table[0][0] = True

    for i in range(n+1):
        table[i][0] = True

    for i in range(1,n + 1):
        v = inset[i-1]

        for j in range(1, X + 1):
            table[i][j] = table[i-1][j]

        if v > X:
            continue

        for j in range(v, X + 1):
           if table[i-1][j-v]:
               table[i][j] = True

    return table[n][X]


print(subsum(table))

for i in range(1, n+1):
    for j in range(X+1):
        print(table[i][j], end="\t")
    print()
