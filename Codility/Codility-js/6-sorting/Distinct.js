function solution(A) {
  const distinct = {};
  let numberOfDistinct = 0;

  A.forEach((number) => {

    if (!distinct[`${number}`]) {
      distinct[`${number}`] = true;
      numberOfDistinct += 1;
    }
  });

  return numberOfDistinct;
}

console.log(solution([2, 2, 1, 3, 1, 1]));
