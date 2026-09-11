def solution(a, b):
    answer = 0
    if a==b: answer = a
    
    elif a>b:
        for nums in range(b, a+1):
            answer += nums
    elif b>a:
        for nums in range(a, b+1):
            answer += nums

    return answer

'''
정수 a 와 b 사이에 있는 모든 수를 포함한 합
반복문 for 를 통해, range(a, b+1) 를 통해 더함
'''