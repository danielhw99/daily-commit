function solution(myString) {
    var answer = '';
    
    for (alpha of myString) {
        if (alpha < 'l') {
            alpha = 'l';
        }
        answer += alpha;
    }
    return answer;
}