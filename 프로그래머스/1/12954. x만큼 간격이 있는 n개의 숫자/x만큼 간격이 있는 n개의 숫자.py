def solution(x, n):
    answer = []
    temp = 0
    for _ in range(n):
        temp += x
        answer += [temp]
    return answer