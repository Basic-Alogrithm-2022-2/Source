def fibo(n):
    #종료 조건
    if n < 3:
        return 1
    else:
        # 피보나치 수열은 앞의 두항의 합이 현재의 합의 값이 됨
        return fibo(n-1) + fibo(n-2)

def fibofor(n):
    n_minus_1 = 1
    n_minus_2 = 1
    n_current = 1

    for i in range(n):
        if i < 2:
            n_current = 1
        else:
            n_minus_2 = n_minus_1
            n_minus_1 = n_current
            n_current = n_minus_1 + n_minus_2
    return n_current

# 1 1 2 3 5 8 13
print(fibo(7))
print(fibofor(7))
