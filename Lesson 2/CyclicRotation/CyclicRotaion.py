def solution(A, K):
    if len(A) == 0:
        return []

    count = len(A) - K % len(A)

    for i in range(count):
        poped = A[0]
        del A[0]
        A.append(poped)
    return A

result = solution([3, 8, 9, 7, 6], 3)
print(result)