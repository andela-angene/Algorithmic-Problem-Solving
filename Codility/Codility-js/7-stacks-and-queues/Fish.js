function solution(A, B) {
  let free = 0;
  const upstream = [];

  A.forEach((size, i) => {
    if (B[i] === 1) {
      upstream.push(size);
    } else {
      let n = upstream.length - 1;
      while (n >= 0) {
        if (upstream[n] > size) break;
        upstream.pop();
        n -= 1;
      }
      if (upstream.length === 0) free += 1;
    }
  });

  return free + upstream.length;
}

console.log(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]));
console.log(solution([4, 2, 5, 2, 1, 3], [0, 0, 1, 0, 0, 0]));
console.log(solution([4, 3, 2, 1, 5], [1, 1, 1, 1, 0]));
console.log(solution([], []));
