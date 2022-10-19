import math
# 함수 정의
def abs_square(a):
    b = a * a
    return int(math.sqrt(b))

# 함수 호출
print(abs_square(-5))
print(abs_square(3))
