from collections import deque
def solution(arr):
    deq = deque()
    for i in range(len(arr)):
        if i==0: 
            deq.append(arr[i]) 
            continue
        elif i>0 and arr[i]!=arr[i-1]:
            deq.append(arr[i])
        else: continue
    return list(deq)