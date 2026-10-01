def solution(n):
    answer = []
    
    answer = list(str(n))
    
    for num in range(len(answer)):
        answer[num] = int(answer[num])
    
    return answer[::-1]