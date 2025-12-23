function solution(arr, k) {
    var answer = [];
    for (values of arr) {
        if (k%2) answer.push(values * k); //홀수
        else answer.push(values + k); //짝수
    }
    return answer;
}