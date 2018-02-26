function cyclic(A, K){
    var len = A.length,
        rotated = [];
    for (var i = 0; i < len; i++){
        rotated[((i + K) % len)] = A[i];
    }
    return rotated;
}

console.log(cyclic([3, 8, 9, 7, 6], 3));
console.log(cyclic([], 3));
console.log(cyclic([3, 8, 9, 7, 6], 78));
console.log(cyclic([3, 8, 9, 7, 6], 0));
console.log(cyclic([3, 8, 9, 7, 6], 1));