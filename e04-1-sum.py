# 연속한 숫자의 합을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 더한 합

# 재귀 호출
def sum(n):
    if n == 0:
        return 0
    return sum(n - 1) + n

# 반복문
def sumfor(n):
    i = 1
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

print(sum(10))   # 1부터 10까지의 합(입력:10, 출력:55)
print(sumfor(10))  # 1부터 100까지의 합(입력:100, 출력:5050)
