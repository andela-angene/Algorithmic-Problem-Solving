function solution(input) {
  const len = input.length;

  let firstTerm = 0;
  while (firstTerm < len - 2) {
    if (input[firstTerm] <= 1) {
      firstTerm += 1;
      continue;
    }

    let pointer = firstTerm + 1;
    while(pointer < len - 1) {
      if (input[pointer] <= 1) {
        pointer += 1;
        continue;
      }

      let multiplier = pointer + 1;
      while(multiplier < len) {
        if (
          input[firstTerm] + input[pointer] > input[multiplier] &&
          input[firstTerm] + input[multiplier] > input[pointer] &&
          input[multiplier] + input[pointer] > input[firstTerm]
        ) return 1;

        multiplier += 1;
      }

      pointer += 1;
    }

    firstTerm += 1;
  }

  return 0;
}


console.log(solution([10, 2, 5, 1, 8, 20]));
console.log(solution([10, 50, 5, 1]));
