# 함수를 이용한 1+2+...+n 모두 더하기
# 함수 정의
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum+=i
    return sum

# 함수 호출
value = get_sum(1, 10)
print('sum =', value)