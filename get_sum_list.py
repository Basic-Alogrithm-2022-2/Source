# 함수를 이용한 리스트 내의 값을 모두 더하기
# 함수 정의
def get_sum(strat, end):
    sum = 0
    for i in values:
        sum+=i
    return sum

values = [1,2,3,4,5,6,7,8,9,10]
# 함수 호출
sum = get_sum(1,len(values))
print(sum)

