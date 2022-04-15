def solution(A):
    array = [0] * 1000001
    
    for i in A:
        if i > 0:
            array[i] += 1
        
    for i in range(1, len(array) + 1):
        if array[i] == 0:
            return i