def solution(s):
    counter = 0
    for alpha in range(len(s)):
        if s[alpha] =='p' or s[alpha] == 'P':
            counter += 1
        elif s[alpha] == 'y' or s[alpha] == 'Y':
            counter -= 1
        else: continue
    return True if counter == 0 else False