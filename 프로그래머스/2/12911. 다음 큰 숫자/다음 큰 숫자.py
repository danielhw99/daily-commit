def solution(n):
    answer = n
    
    while answer>=n:
        answer += 1
        a = str(bin(answer)).count('1')
        b = str(bin(n)).count('1')
        if a==b:
            break
    
    return answer