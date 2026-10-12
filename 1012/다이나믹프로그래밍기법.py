n, X = map(int, input().split())
inset = list(map(int, input().split()))
table = [[False] * (X + 1) for _ in range(n + 1)]

def subsum(table):
    v = 0
    table[0][0] = True

    for i in range(len(inset)):
        table[0][i] = True
    for i in range(1,n):
        v = 
    if v > X:
        v = X
    for j in range(1,v):
        table[][] = table[][]
    for j in range(v, X+1):
        if table[][]:
            table[][] = True
            continue
        table[][] = table[][]
    return table[][]


print(subsum(table))
for i in range(X+1):
    for j in range(X+1):
        print(table[i][j], end="\t")
    print()
