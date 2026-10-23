def solution(arr):
    if len(arr)==1:
        return [-1]
    
    answer = []
    minval = min(arr)
    index = arr.index(minval)
    answer = arr[:index] + arr[index+1:]
    return answer