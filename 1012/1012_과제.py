
def MCS(A, B):      # Most Common Strings(최대 공통 문자열)
    # A + 1만큼의 행과 B + 1만큼의 열을 가지는 2차원 배열 table을 생성하고, 모든 값을 0으로 초기화.
    table = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i-1] == A[j-1]:    # 같은 글자일 때는 대각선 개수 + 1
                table[i][j] = table[i-1][j-1] + 1
            else:                   # 다른 글자일 때는 왼쪽이나 위 쪽 중 큰 값
                table[i][j] = max(table[i-1][j], table[i][j-1])

    print("first string: " + B)
    print("second string: " + A)
    print("     ", end = "")
    for i in A:                     # A 문자열의 알파벳 한 개 단위로 i 변수에 선언. 
        print(i, end = "  ")        # A의 알파벳들을 순서대로 출력하고 간격 유지.
    print()                         # 줄바꿈
    
    for i in range(len(B)):                 # B 행 크기 만큼 반복
        print(B[i] + " :", end ="  ")           # B의 알파벳들을 한 줄 씩 출력
        for j in range(len(A)):             # A 열 크기 만큼 반복
            print(table[i+1][j+1], end ="  ")   # 2차원 배열의 값들을 출력
        print()                             # 줄바꿈


A = "abcacdefgadb"
B = "acbcdgadfgdze"

MCS(A,B)