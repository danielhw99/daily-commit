def solution(s):
    print(len(s))
    if len(s)==4 or len(s)==6: pass
    else: return False
    for i in s:
        if i>"9":
            return False
        else: continue
    return True