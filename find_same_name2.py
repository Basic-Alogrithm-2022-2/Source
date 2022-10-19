# 함수 정의
def find_same_name(a):
    result = set()
    # result = []
    for i in range(0,n):
        for j in range(i+1,n):
            if names[i] == names[j]:
                result.add(names[i])
                # result.append(names[i])
    return result

names = ['Tom', 'Jerry', 'Mike', 'Tom', 'Jerry', 'Tom']
n = len(names)

# 함수 호출
result = find_same_name(names)
print(result)