def solution(x):
    s=str(x)
    sum = 0
    for i in range(len(s)):
        print(int(s[i]))
        sum += int(s[i])
    print(sum)
        
    return True if x%sum==0 else False