import random

def fibo(n):
    a, b = 0, 1
    fibo_set = set()
    fibo_set.add(1)

    while b <= n:
        a, b = b, a + b
        fibo_set.add(b)
    return fibo_set

def solution(A):
    fibo_set = fibo(len(A))
    A.append(1)
    dp = [0] * len(A)

    for i in range(len(A)):
        if A[i] == 1 and i + 1 in fibo_set:
            dp[i] = 1
            continue
        
        if A[i] == 1 and dp[i] < 1:
            min_count = 100001
            isExist = False
            for num in fibo_set:
                if i - num < 0 or dp[i - num] < 1:
                    continue
                if A[i - num] == 1:
                    min_count = min(min_count, dp[i - num])
                    isExist = True
            if isExist:
                dp[i] = min_count + 1
    return dp[-1] if dp[-1] != 0 else -1


result = solution([1 for _ in range(100000)])
print(result)