def solution(n):
    answer = 1
    while answer <= 1000:
        if n/answer == answer:
            return 1
        else: answer+= 1
    return 2