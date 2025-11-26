from collections import deque

def solution(p, loc):
    answer = 0
    q = deque()
    
    for e in p:
        q.append(e)
        
    t_val = p[loc]
    mx = 0
    cnt = 0
    while(q):
        mx = max(q)
        
        if q[0] < mx:
            v = q.popleft()
            q.append(v)
            loc = (loc-1) % len(q)
        elif q[0] >= mx:
            
            cnt += 1
            
            if loc == 0:
                return cnt
            
            loc -= 1
            q.popleft()
            
    return answer