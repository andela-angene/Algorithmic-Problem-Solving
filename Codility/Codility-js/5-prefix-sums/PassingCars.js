function solution(A){
    let ones = 0,
        zeros = 0,
        minus = 0,
        N = A.length;
    
    for (let i = 0; i < N; i++){
        if (A[i]){
            ones++;
        }else{
            zeros++;
            minus += ones;
        }
        if (ones * zeros - minus > 1000000000) return -1;
    }

    return ones * zeros - minus;
}

console.log(solution([0,1,0,1,1]));
console.log(solution([]));
console.log(solution([0,1,0,1,1,0,1]));
console.log(solution([0,1]));
console.log(solution([1]));
console.log(solution([1,0]));