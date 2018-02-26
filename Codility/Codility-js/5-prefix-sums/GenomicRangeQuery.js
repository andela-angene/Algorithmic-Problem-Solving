function solution(S, P, Q) {
  const minValues = [];

  P.forEach((val, index) => {
    const cut = S.slice(val, Q[index] + 1);
    if (cut.indexOf('A') !== -1){
      minValues.push(1);
    } else if (cut.indexOf('C') !== -1) {
      minValues.push(2);
    } else if (cut.indexOf('G') !== -1) {
      minValues.push(3);
    } else {
      minValues.push(4);
    }
  });

  return minValues;
}

console.log(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]));
