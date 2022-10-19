# 함수 정의
def find_max(a):
    max_idx=0
    for i in range(1,len(a)):
        if a[i] > a[max_idx]:
            max_idx = i
    return (max_idx, a[max_idx])

def find_min(a):
    min_idx=0
    for i in range(1,len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx, a[min_idx]

a = [24, 634, 36, 14, 53, 125, 1, 222, 555, 99]
# 함수 호출
print(find_max(a))
print('최대값은', ' INDEX=', find_max(a)[0])
print('최대값은', ' VALUE=', find_max(a)[1])

print(find_min(a))
print('최소값은', ' INDEX=', find_min(a)[0])
print('최소값은', ' VALUE=', find_min(a)[1])

