import time
import tracemalloc

def memory_print(stats):
    for i in stats[:10]:
        print(i)

def solution(A):
    start = time.time()
    tracemalloc.start()

    arr_len = len(A)
    peak_arr = []
    mok_arr = []

    for i in range(1, arr_len - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peak_arr.append(i)
    
    peak_len = len(peak_arr)

    if peak_len == 0:
        return 0
    
    for i in range(1, int(arr_len ** (1/2)) + 1):
        if arr_len % i == 0:
            if i <= peak_len:
                mok_arr.append(i)
            if arr_len // i <= peak_len:
                mok_arr.append(arr_len // i)

    mok_arr = sorted(mok_arr, reverse=True)
    
    for i in mok_arr:
        count = 0
        block = [False] * i
        for j in range(peak_len):
            index = peak_arr[j] // (arr_len // i)
            if not block[index]:
                block[index] = True
                count += 1
        if count == i:
            print(f"{time.time() - start:.5f} sec")
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            memory_print(top_stats)
            return i

    print(f"{time.time() - start:.5f} sec")
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    memory_print(top_stats)
    return i


result = solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
print(result)