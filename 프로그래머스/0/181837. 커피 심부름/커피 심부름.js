var coffee = {
    ame : 'americano',
    lat : 'latte',
    americano : 4500,
    latte : 5000
    }

function solution(orders) {
    var answer = 0;
    for (var order of orders) {
        if (order.includes(coffee.ame)) {
            answer += coffee.americano;
        } else if (order.includes(coffee.lat)) {
            answer += coffee.latte;
        } else {
            answer += coffee.americano;
        }
    }
    
    return answer;
}