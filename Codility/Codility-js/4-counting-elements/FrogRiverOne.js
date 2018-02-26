function solution(X, A) {
    var arr = [],
        count = 0;

    for (var i = 0; i < A.length; i++){
        var c = A[i];
        if ( c <= X){
            if (!arr[c]){
                arr[c] = true;
                count++;
            }
        }

        if (X === count) return i;
    }
    return -1;
}

// function solution(X, A){
//     var N = A.length,
//         count = [],
//         position = 0;

//         for (var i = 0; i <= X; i++) {count.push(false);}

//         for (var i = 0; i < N; i++){
//             if (!count[A[i]]){
//                 count[A[i]] = true;
//                 position++;
//             }

//             if (position === X) return i;
//         }

//         return -1;
// }

console.log(solution(5, [1, 3, 1, 4, 2, 5, 3, 4]));
console.log(solution(3, [1, 3, 1, 3, 2, 3]));