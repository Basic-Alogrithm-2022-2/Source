# 반복문
# 시간의 복잡도는?
def factfor(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
        print(f)
    return f

# 재귀 호출
# 시간의 복잡도는 ?
def fact(n):
    if n <= 1:
        return n
    else:
        return n * fact(n-1)

print('반복문', factfor(5))
print('재귀호출', fact(5))
