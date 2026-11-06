def solution(s):
    words = s.split(" ")
    answer = ''
    
    for word in words:
        for i in range(len(word)):
            if i%2==0:#짝수
                answer += word[i].upper()
            elif i%2!=0:
                answer += word[i].lower()
        answer += " "
        print(answer)
    
    return answer[:-1]