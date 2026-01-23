def solution(t, p):
    answer = 0
    length = len(p)
    print(length)
    comp = []
    
    for i in range(len(t)-(length-1)):
        comp += [t[i:i+length]]
    
    for compare in comp:
        if compare <= p:
            answer += 1
    
    
    
    return answer

'''
t의 부분 문자열의 리스트를 구한다.
for comp in [t의 부분 문자열]:
    p 와 comp 가 같으면 answer을 1 더한다.
    
t의 부분 문자열 리스트 구하기
- t의 길이를 len_t 라할 때,
for i 인덱스 0 부터 (len_t - 2):
    comp = t[i:i+2]
    
'''