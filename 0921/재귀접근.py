## 재귀접근 방법

##1. 종료 조건이 있어야 한다. (없으면 무한 반복)
## 전체 작업의 일부만 수행하고 나머지는 재귀 호출에 위임

## 1부터 n까지 합을 재귀로 구현한 함수

def sigma(n):
    if n==1:
        return 1
    else:
        return sigma(n-1) + n

## 재귀함수의 호출에 따른 메모리

def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n-1)



##선행 재귀(head recursion)

def printup(n):
    if n > 0:
        printup(n-1)
        print(n)
##printup(4) [결과: 1, 2, 3, 4]

def printup2(n):
    if n > 0:
        print(n)
        printup2(n-1)
##printup2(4) [결과: 4, 3, 2, 1]

def recur(n):
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

##재귀 기법
    ## 선행 재귀(head recursion)
    ## 후행 재귀(tail recursion)


##메모제이션
    ##재귀 함수의 한계: 계산 한 값을 반복적으로 계산
    ##n이 커질 수록 계싼 회수는 매우 많아짐
    ##개선
        ##같은 계산은 1회만 수행하고 여러번 계산하지 않도록 조치
        ##fibo 함수가 해답을 얻으면 그것을 메모해둠

##메모제이션 VS 재귀
memo = [0]*1000
memo = [1,1]+memo
cnt=0
def fibo(n):
    global cnt
    cnt += 1
    if memo[n]==0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]
##for i in range(1,11):
    print(i, fibo(i), cnt)

print("--------")
cn2=0
def fibo2(n):
    global cnt2
    cnt2 += 1
    if n==0 or n==1:
        return 1
    return fibo2(n-1)+fibo2(n-2)
#for i in range(1,11):
    print(i, fibo2(i), cnt2)


##하노이 탑
    ##문제: 쌓아 놓은 원반을 최소의 회수로 옮기기 위한 알고리즘
    ##제약 조건
        ##한 번에 하나의 원반을 움직일 수 있다.
        ##지름이 큰 원반은 작은 원반 위에 쌓을 수 없다.

def hanoi(n,A,B,C):
    if n > 0:
        hanoi(n-1,A,C,B)
        print(f"{n}원반을 {A} -> {C}로 이동")
        hanoi(n-1,B,A,C)
hanoi(3,'A','B','C')



##홍수 채우기
    ##의사 코드
        ## 교체될 색상과 교체할 색상이 같다면 반환
        ## 탐색위치의 색상과 교체될 색상이 같지 않다면 반환
        ## 색상 교체
        ## 홍수채우기 - 동쪽으로 이동, 교체될 색상, 교체할 색상
        ## 홍수채우기 - 서쪽으로 이동, 교체될 색상, 교체할 색상
        ## 홍수채우기 - 남쪽으로 이동, 교체될 색상, 교체할 색상
        ## 홍수채우기 - 북쪽으로 이동, 교체될 색상, 교체할 색상

def fill(y,x, color, targetColor):
    if grid[y][x] != color or gird [y][x] == targetColor:
        return

    grid[y][x] = targetColor

    for ny, nx in [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]:
        if not (0 <= ny < rows) or not (0 <= nx < cols):
            continue
        fill(ny,nx,color,targetColor)