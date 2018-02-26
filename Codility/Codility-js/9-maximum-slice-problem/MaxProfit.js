function solution(A) {
  let profit = 0;
  let currentMin = A[0];

  A.forEach((item) => {
    if (item < currentMin) {
      currentMin = item;
    } else if ((item - currentMin) > profit) {
      profit = item - currentMin;
    }
  });

  return profit;
}

console.log(solution([8]));
console.log(solution([100, 200, 10, 190]));
console.log(solution([200, 150, 100, 100]));
console.log(solution([21011, 21123, 21366, 21013, 21367]));
