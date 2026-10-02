def solution(n):
    answer = 0
    dummy=[]
    for num in str(n):
        dummy += num
    dummy.sort()
    dummy=dummy[::-1]
    for i in range(len(dummy)):
        answer += int(dummy[i]) * 10 ** (len(dummy)-i-1)
    return answer