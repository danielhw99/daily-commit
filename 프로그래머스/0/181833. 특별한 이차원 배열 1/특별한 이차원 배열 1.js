function solution(n) {
    var answer = new Array(n);

    for (var i = 0; i < answer.length; i++) {
        answer[i] = new Array(n);
    }
    for (i=0;i<n;i++) {
        for(j=0;j<n;j++) {
            if (i==j) answer[i][j] = 1;
            else answer[i][j] = 0;
        }
    }
    return answer;
}