def solution(s):
    answer = True
    
    counter = 0
    for c in s:
        if counter == 0:
            if c != '(':
                return False
            counter += 1
        else:
            if c == '(':
                counter += 1
            elif c == ')':
                counter -= 1
        if counter < 0: return False
    if counter != 0:
        answer = False
    
    return answer