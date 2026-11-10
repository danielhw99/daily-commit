def solution(s):
    answer = []
    dict = {}
    
    for i in range(len(s)):
        if s[i] not in dict:
            answer.append(-1)
            dict[s[i]]=[i]
            continue
        if s[i] in dict:
            diff=100000
            for j in dict[s[i]]:
                diff = min(diff, abs(j-i))
            answer.append(diff)
            dict[s[i]].append(i)
        
    print(dict)
    
    return answer