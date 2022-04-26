import time

def solution(N):
    start = time.time()
    
    array = []
    answer = 0
    count = 0
    
    while N >= 2:
        namuji = N % 2
        N //= 2
        array.append(namuji)
    array.append(N)
    array.reverse()

    for i in array:
        if i == 1:
            if count > answer:
                answer = count
            count = 0
        else:
            count += 1

    print(f"{time.time() - start:.5f} sec")

    return answer


solution(1376796946)
solution(1073741825)
solution(1610612737)