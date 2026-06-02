def solution(n):
    answer = 0
    key = 1
    
    while key<=n:
        if key <= n and n%key==0:
            answer += 1
        key += 1
    return answer