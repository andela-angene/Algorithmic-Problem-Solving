function equil(A){
    var diff    = [],
        sum     = A.reduce(function(a, b){return a + b;}, 0),
        subSum  = 0,
        len     = A.length - 1;
    for (var i = 0; i < len; i++){
        subSum += A[i];
        diff.push(Math.abs(sum - subSum*2));
    }
    return Math.min.apply(null, diff);
}

function equi(A){
    var sum     = A.reduce(function(a, b){return a + b;}, 0),
        subSum  = 0,
        len     = A.length;
    for (var i = 0; i < len; i++){
        subSum += (A[i-1] === undefined) ? 0 : A[i-1];
        if (sum - subSum*2 - A[i] === 0) return i;
    }
    return -1;
}

// console.log(equil([3, 1, 2, 4, 3]));
// console.log(equi([3,9]));
console.log(equi([200, 300, -300]));
console.log(equi([-1, 3, -4, 5, 1, -6, 2, 1]));
console.log(equi( [1, 2, -3, 0]));