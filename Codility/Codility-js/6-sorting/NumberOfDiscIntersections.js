function solutionA(A) {
  const len = A.length;
  let counter = 0;
  let maxReach = 0;

  let pointer = 0;
  while (pointer < len) {
    const currentValue = A[pointer];

    if (maxReach < pointer - currentValue) {
      pointer += 1;
      continue;
    }

    if (currentValue + pointer > maxReach) maxReach = currentValue + pointer;

    let iterator = 0;
    while (iterator < pointer) {
      if ((currentValue + A[iterator]) >= pointer - iterator) {
        counter += 1;
        if (counter > 10000000) return -1;
      }

      iterator += 1;
    }

    pointer += 1;
  }

  return counter;
}

function solution(A) {
  const len = A.length;
  let counter = 0;
  let pointer = 0;
  const maxCounter = {};

  while (pointer < len) {
    const maxReach = (A[pointer] + pointer) > (len - 1) ? len - 1: pointer + A[pointer];
    counter += maxReach - pointer;
    maxCounter[`${maxReach}`] ? maxCounter[`${maxReach}`] += 1 : maxCounter[`${maxReach}`] = 1;

    let backRadius = (pointer - A[pointer]) < 0 ? pointer : A[pointer];
    let iterator = 0;
    while(iterator < backRadius) {
      const loc = pointer - iterator -1;
     if (maxCounter[`${loc}`]) counter += maxCounter[`${loc}`];
      iterator += 1;

      if (counter > 10000000) return -1;
    }

    pointer += 1;
  }

  return counter;
}

console.log(solution([1, 5, 2, 1, 4, 0]));
console.log(solution([0, 0, 0, 0]));
console.log(solution([1, 5, 2, 1]));
