function solution(A) {
  let minIndex = 0,
      minAverage = (A[0] + A[1])/2;
  A.forEach((val, index, arr) => {
    let sum = val + arr[index + 1],
        average = (sum)/2,
        secondAverage = (sum + arr[index + 2])/3;
    if (average < minAverage || secondAverage < minAverage) {
      minIndex = index;
      minAverage = Math.min(average, secondAverage);
    }
  });
  return minIndex;
}

console.log(solution([4,2,2,5,1,5,8]));
