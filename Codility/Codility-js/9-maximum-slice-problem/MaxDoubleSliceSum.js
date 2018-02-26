function solution(A) {
  let maxSum = 0;
  let currentSum = 0;

  let compare = A[1];

  let pointer = 2;
  while (pointer < A.length - 1) {
    const value = A[pointer];

    if (value < compare) {
      currentSum += compare;
      compare = value;
    } else if (currentSum + value >= value) {
      currentSum += value;
    } else {
      if (value > maxSum) maxSum = value;
      currentSum = 0;
      compare = A[pointer];
    }

    if (currentSum > maxSum) maxSum = currentSum;
    pointer += 1;
  }

  return maxSum;
}
console.log(solution([3, 2, 6, -1, 4, 5, -1, 2]));
console.log(solution([-3, 2, 3, -1, 1, -2, 3, 4]));
console.log(solution([3, 2, -1, 6]));
console.log(solution([-3, -32, -26, -31, 4, 5, -21, -42]));

