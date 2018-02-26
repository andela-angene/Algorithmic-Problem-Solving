function solution(A) {
    var arr = [];
    for (var i = 0; i < A.length; i++){
        if (arr[A[i]]) return 0;
        arr[A[i]] = true;
    }
    for (var i = 1; i < arr.length; i++){
        if(!arr[i]) return 0;
    }
    return 1;
}

console.log(solution([1,2,3,3,4]));