function solution(A) {
  let maxSum = A[0];
  let currentSum = A[0];

  let pointer = 1;
  while (pointer < A.length) {
    const value = A[pointer];

    currentSum = (currentSum + value > value) ? currentSum + value : value;

    if (currentSum > maxSum) maxSum = currentSum;
    pointer += 1;
  }

  return maxSum;
}

describe('MaxSliceSum', () => {
  it('', () => {
    expect(solution([3, 2, -6, 4, 0])).toBe(5);
  });
  it('', () => {
    expect(solution([0, -2])).toBe(0);
  });
});

// console.log(solution([3, 2, -6, 4, 0]));
// console.log(solution([0, -2]));
// console.log(solution([-2]));
// console.log(solution([5, -2, 10, 3, -25, 12, 6]));
// console.log(solution([-5, -2, -10, -3, -25, -12, -6]));
