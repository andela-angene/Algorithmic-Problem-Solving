function solution(A){
    var sum = 1; 
    var aSum = 0;
    for  (var i = 0; i < A.length; i++){
        sum = sum + i + 2;
        aSum += A[i];
    }
    return sum - aSum;
}

console.log(solution([]));

console.log(solution([2, 4, 1]));

console.log(solution([6]));

console.log(solution([100, 102]));