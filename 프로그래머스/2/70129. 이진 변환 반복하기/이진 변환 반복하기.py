def solution(s):
    
    binary_changed = 0
    deleted_zeroes = 0
    after=len(s)
    while after!=1:
        
        zeroes = s.count('0')
        after = len(s)-zeroes
        deleted_zeroes += zeroes
        
        s=format(after, 'b')
        
        binary_changed += 1
    return [binary_changed, deleted_zeroes]
        

'''
이진 변환
문자열을 읽어와서 제거할 0의 개수를 count
제거 후 길이=기존길이-count
해당 숫자를 다시 이진변환
반복

-반복할 때 [이진변환 횟수,제거한 0의 개수 누적]
'''