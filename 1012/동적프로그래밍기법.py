def dynamicInter(A,B,C):
    if len(A) + len(B) != len(C):
        return False
    A = [''] + list(A)      # A = [ '', 'b', 'b', 'c']
    B = [''] + list(B)      # B = [ '', 'b', 'b', 'c', 'a']

    # A 크기의 행, B 크기의 열인 2차원 배열 생성 & 동시에 모든 칸을 False로 초기화
    table = [[False] * (len(B)) for _ in range(len(A))]
    # 아무 문자도 사용되지 않는 table[0][0]은 True로 초기화
    table[0][0] = True

    # 1. B의 문자만으로 C를 만들 수 있는지 확인
    for i in range(1,len(B)):
        if C[i-1] == B[i] and table[0][i-1]:
            table[0][i] = True
    # 2. A의 문자만으로 C를 만들 수 있는지 확인
    for i in range(1,len(A)):
        if C[i-1] == A[i] and table[i-1][0]:
            table[i][0] = True
    # 3. A와 B의 문자를 섞어서 C를 만들 수 있는지 확인
    for i in range(1,len(A)):
        for j in range(1,len(B)):
            if B[j] == C[i+j-1] and table[i][j-1]:
                table[i][j] = True
                continue
            if A[i] == C[i+j-1] and table[i-1][j]:
                table[i][j] = True

    for i in table:
        for j in i:
            print(j, end=" ")
        print()
    return table[len(A)-1][len(B)-1]

A = "aabcedf"
B = "bdceseg"
C = "abadbceeseedgf"
print(dynamicInter(A,B,C))