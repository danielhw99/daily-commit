def solution(s):
    if s=='' or s==' ':
        return ''
    answer = ''
    words = s.split(" ")
    for word in words:
        word = word.lower()
        if word.isalpha() and word[0].isalpha():
            word = word[0].upper() + word[1:]
        answer += word
        answer += " "
        
    return answer[:-1]