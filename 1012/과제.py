def LCS(A, B):
    table = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i - 1] == A[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    print("first string:", B)
    print("second string:", A)

    print("    ", end="")
    for c in A:
        print(c, end=" ")
    print()

    for i in range(1, len(B) + 1):
        print(B[i - 1], ":", end=" ")
        for j in range(1, len(A) + 1):
            print(table[i][j], end=" ")
        print()


A = "abcacdefgadb"
B = "acbcdgadfgdze"

LCS(A, B)