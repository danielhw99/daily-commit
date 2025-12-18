function odd(val1, val2) {
    return val1*val1 + val2*val2;
}

function even(val1, val2) {
    return Math.abs(val1-val2);
}

isEven = val => val%2==0?true:false;

function solution(a, b) {
    var answer = 0;
    var isAEven = isEven(a)
    var isBEven = isEven(b);
    
    if (isAEven && isBEven) {
        answer = even(a, b);
    } else if (!isAEven && !isBEven) {
        answer = odd(a, b);
    } else {
        answer = 2 * (a + b);
    }
    return answer;
}