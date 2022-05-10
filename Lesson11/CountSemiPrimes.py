import random
import psutil
import time
import os


start = float()

def func(n):
    F = [0] * (n + 1)
    array = []
    i = 2
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1

    for j in range(2, len(F)):
        if F[j] == 0:
            array.append(j)

    return array


def solution(N, P, Q):
    array = func(N)
    semi = [0] * (N + 1)
    count_arr = [0] * (N + 1)
    answer = []
    for i in range(len(array)):
        if i * 2 > N:
            break
        for j in range(i, len(array)):
            if array[i] * array[j] <= N:
                semi[array[i] * array[j]] = array[i] * array[j]
            else:
                break        
    sum = 0
    for i in range(4, N + 1):
        if semi[i] != 0:
            sum += 1
        count_arr[i] = sum
            
    for i in range(len(P)):
        answer.append(count_arr[Q[i]] - count_arr[P[i]-1])
    
    return answer






def before_memory():
    # BEFORE code
    print(f"== {0:2d} exec")
    # general RAM usage
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    print(f"BEFORE CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
    print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")


def after_memory():
    # AFTER  code
    memory_usage_dict = dict(psutil.virtual_memory()._asdict())
    memory_usage_percent = memory_usage_dict['percent']
    print(f"AFTER  CODE: memory_usage_percent: {memory_usage_percent}%")
    # current process RAM usage
    pid = os.getpid()
    current_process = psutil.Process(pid)
    current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
    print(f"AFTER  CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")
    print("--"*30)


def check_start_time():
    start = time.process_time()

def check_end_time():
    print(f"Total Time Elapsed : {int(round((time.process_time() - start) * 1000))}ms")  


p = []
q = []

for i in range(30000):
    p.append(1)
    q.append(29999)

before_memory()
check_start_time()

solution(50000, p, q)

after_memory()
check_end_time()