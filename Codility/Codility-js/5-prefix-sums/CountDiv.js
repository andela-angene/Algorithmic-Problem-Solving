function solution(A, B, K) {
    var mod = (A % K === 0) ? K : A % K;
    var diff = A + (K - mod);
    if (diff > B) return 0;
    return Math.floor((B - diff)/K) + 1;
}

console.log(solution(6, 11, 2));
console.log(solution(6, 6, 2));
console.log(solution(5, 5, 2));
console.log(solution(5, 13, 12));