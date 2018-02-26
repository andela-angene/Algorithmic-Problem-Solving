function solution(A) {
  function maxOfMultiples(input) {
    const result = [];
    const len = input.length;

    let firstTerm = 0;
    while (firstTerm < len - 2) {

      let pointer = firstTerm + 1;
      while(pointer < len - 1) {

        let multiplier = pointer + 1;
        while(multiplier < len) {
          result.push(input[firstTerm] * input[pointer] * input[multiplier]);
          multiplier += 1;
        }

        pointer += 1;
      }

      firstTerm += 1;
    }

    return Math.max(...result);
  }

  A.sort((a, b) => a -b);
  const totalLen = A.length;
  if (totalLen < 5) {
    return maxOfMultiples(A);
  }

  return maxOfMultiples([A[totalLen - 1], A[totalLen - 2], A[totalLen - 3], A[0], A[1]]);
}


console.log(solution([-6, 3, 4, 5]));
console.log(solution([-6, 4, 5, -2]));
console.log(solution([6, 3, 4, 5, 2]));
console.log(solution([-3, 1, 2, -2, 5, 6]))
console.log(solution([1000, 999, 998, 997, -1000, -999, -998, -997,]))
// console.log([1000, 999, 998, 997, -1000, -999, -998, -997].sort((a, b) => a -b));
