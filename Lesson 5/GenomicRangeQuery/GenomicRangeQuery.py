import time
import tracemalloc

def solution(S, P, Q):
    start = time.time()
    tracemalloc.start()

    array = []

    for i in range(len(P)):
        set_str = set(S[P[i]:Q[i] + 1])

        if 'A' in set_str:
            array.append(1)
        elif 'C' in set_str:
            array.append(2)
        elif 'G' in set_str:
            array.append(3)
        else:
            array.append(4)

    print(f"{time.time() - start:.5f} sec")
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    for i in top_stats[:10]:
        print(i)

    return array

result = solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
print("Result :", result)