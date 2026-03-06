def solution(s1, s2):
    answer = 0
    for element in s2:
        if element in s1:
            answer += 1
    return answer