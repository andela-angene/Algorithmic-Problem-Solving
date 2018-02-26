function solution(A) {
  function computeEqui(item, equi, set, length) {
    set[item] = set[item] ? set[item] + 1 : 1;
    if (set[item] > equi.num) {
      equi = { num: set[item], value: item };
    } else if (set[item] === equi.num) {
      equi.value = false;
    }

    if (equi.num <= Math.floor(length / 2)) equi.value = false;

    return equi;
  }

  let equi = { num: 0, value: false };
  let set = {};
  const equiCollection = [];
  let counter = 0;

  A.forEach((item, i) => {
    equi = computeEqui(item, equi, set, i + 1);

    equiCollection.push(equi.value);
  });

  equi = { num: 0, value: false };
  set = {};

  const len = A.length;
  let pointer = len - 1;
  while (pointer > 0) {
    equi = computeEqui(A[pointer], equi, set, len - pointer);

    if (equi.value !== false && equi.value === equiCollection[pointer - 1]) {
      counter += 1;
    }
    pointer -= 1;
  }

  return counter;
}

console.log(solution([4, 3, 4, 4, 4, 2]));
console.log(solution([-40000000000000000000000, 3, -40000000000000000000000, -40000000000000000000000, -40000000000000000000000, 3000000000000000000000]));
console.log(solution([4, 4, 2, 5, 3, 4, 4, 4]));
