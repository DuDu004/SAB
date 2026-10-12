def dynamicInter(A,B,C):
    if len(A) + len(B) != len(C):
        return False
    A = [''] + list(A)
    B = [''] + list(B)
    C = [''] + list(C)
    table = [[False] * (len(B)) for _ in range(len(A))]
    table[0][0] = True
    for i in range(1,len(B)):
        if C[i-1] == B[i] and table[0][i-1]:
            table[0][i] = True
    for i in range(1,len(A)):
        if C[i-1] == A[i] and table[i-1][0]:
            table[i][0] = True
    for i in range(1,len(A)):
        for j in range(1,len(B)):
            if B[j] == C[i+j-1] and table[i][j-1]:
                table[i][j] = True
                continue
            if A[i] == C[i+j-1] and table[i-1][j]:
                table[i][j] = True
    return table

A = "bbc"
B = "bbca"
C = "bbbbcac"
print(dynamicInter(A,B,C))