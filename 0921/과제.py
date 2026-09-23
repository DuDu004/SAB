def favorite(List, n, flag):
    if n > 3:
        return 0

    most = 0

    for i in range(4):
        if flag[i] == 1:
            continue
        flag[i] = 1
        
        sum = List[n][i] + favorite(List, n+1, flag)
        if sum > most:
            most = sum

        flag[i] = 0

    return most


List = [list(map(int,input().split())) for _ in range(4)]
n = 0
flag = [0, 0, 0, 0]

print(favorite(List, n, flag))

