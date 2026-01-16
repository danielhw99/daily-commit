def solution(array, n):
    answer = 0
    for ele in array:
        if ele == n:
            answer += 1
    return answer