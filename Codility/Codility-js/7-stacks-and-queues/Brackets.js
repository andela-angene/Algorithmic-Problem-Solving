function solution(S) {
  const nests = {
    '(': ')',
    '[': ']',
    '{': '}'
  };
  const toBeClosed = [];

  let pointer = 0;
  while (pointer < S.length) {
    const current = S[pointer];
    if (nests[current]) {
      toBeClosed.push(nests[current]);
    } else if (current === toBeClosed[toBeClosed.length - 1]) {
      toBeClosed.pop();
    } else {
      return 0;
    }
    pointer += 1;
  }
  return toBeClosed.length > 0 ? 0 : 1;
}

console.log(solution('{[()()]}'));
console.log(solution('([)()]'));
console.log(solution(''));
console.log(solution(']['));
