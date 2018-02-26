function solution(S) {
  const toBeClosed = [];

  let pointer = 0;
  while (pointer < S.length) {
    const current = S[pointer];
    if (current === '(') {
      toBeClosed.push(')');
    } else if (current === toBeClosed[toBeClosed.length - 1]) {
      toBeClosed.pop();
    } else {
      return 0;
    }
    pointer += 1;
  }
  return toBeClosed.length > 0 ? 0 : 1;
}

console.log(solution('(()(())())'));
console.log(solution('())'));
console.log(solution(')'));
console.log(solution('(())'));
console.log(solution(''));
