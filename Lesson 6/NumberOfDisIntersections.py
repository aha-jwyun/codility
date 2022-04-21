import time
import tracemalloc

def print_(stats):
    for i in stats[:10]:
        print(i)

def solution(A):
    start = time.time()
    tracemalloc.start()

    array = []

    for i in range(len(A)):
        array.append([i - A[i], False])
        array.append([i + A[i], True])
    array = sorted(array)

    unclosed_circle = 0
    intersect = 0
    over = False

    for point in array:
        if point[1]:
            unclosed_circle -= 1
        else :
            intersect += unclosed_circle
            unclosed_circle += 1
            if intersect > 10000000:
                over = True 

    print(f"{time.time() - start:.5f} sec")

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print_(top_stats)

    if over:
        return -1    
    
    return intersect