function solution(A) {
    var arr = [];
    for (var i = 0; i < A.length; i++){
        arr[A[i]] = true;
    }
    for (var i = 1; i <= arr.length; i++){
        if(!arr[i]) return i;
    }
    return 1;
}


console.log(solution([-1,-2,-4]));