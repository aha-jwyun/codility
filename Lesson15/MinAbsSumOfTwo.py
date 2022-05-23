def solution(A):
    A = sorted(A, key = lambda x : abs(x))

    min_value = abs(A[0] + A[0])

    for i in range(len(A) - 1):
        min_value = min(min_value, abs(A[i] + A[i + 1]))

    return min_value

result = solution([1,  4, -3])
print(result)
result = solution([-8, 4, 5, -10, 3])
print(result)