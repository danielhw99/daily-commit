function solution(array) {
    var answer = 0;
    for(let i=0;i<array.length;i++) {
        for (item of array[i].toString()){
            if (item == '7') {
                answer += 1
            }
        }
    }
    return answer;
}