def solution(rank, attendance):
    answer = 0
    ans = {}
    
    
    count = 0
    for i in range(len(attendance)):
        if(attendance[i]): # True면
            print(i, " : " , rank[i])
            ans[i] = rank[i]
    val = list(ans.values())
    val.sort()
    
    for k, v in ans.items():
        if v == val[0]:
            answer += k*10000
        elif v == val[1]:
            answer += k*100
        elif v == val[2]:
            answer += k
    
    
    return answer