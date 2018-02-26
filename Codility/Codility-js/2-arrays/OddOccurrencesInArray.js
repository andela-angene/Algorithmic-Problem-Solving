function oddOccurrance(A){
    A = A.sort();
    var count = 0;
    for (var i = 0; i < A.length; i++){
       count++;
       if(A[i] !== A[i + 1]){
           if(count % 2 === 1) return A[i];
           count = 0;
       }
    }
}

console.log(oddOccurrance([20, 2, 3, 6, 6, 3, 2, 7 ,2, 2, 7, 20, 12, 12, 12]));
console.log(oddOccurrance([2, 3, 3, 2, 5]));
console.log(oddOccurrance([2, 3, 3, 2, 5, -2, 5]));