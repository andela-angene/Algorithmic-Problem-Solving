function solution(N, A) {
    var arr = [];
    for (var i = 0; i < N; i++) arr.push(0);
    var M = A.length,
        max = 0,
        base = 0;

    for (var i = 0; i < M; i++) {
        var K = A[i];
        
        if (K > 0 && K <= N) {
            var C = arr[K-1] + 1;
            arr[K-1] = (base >= C) ? base + 1 : C;

            if (arr[K-1] > max) max = arr[K-1];
        }
        if (K === N + 1){
            base = max;
        }
    }

    for (var i = 0; i < N; i++){
        if (arr[i] < base) arr[i] = base;
    }

    return arr;
}

console.log(solution(5, [3,4,4,6,1,4,4]));

console.log(solution(5, [2, 6,6,6]));