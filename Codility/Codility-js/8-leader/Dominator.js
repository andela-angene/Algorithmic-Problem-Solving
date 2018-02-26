function solution(A) {
  function computeEqui(item, equi, set, length) {
    set[item] = set[item] ? set[item] + 1 : 1;
    if (set[item] > equi.num) {
      equi = { num: set[item], value: item };
    } else if (set[item] === equi.num) {
      equi.value = false;
    }

    if (equi.num <= length / 2) equi.value = false;

    return equi;
  }

  let equi = { num: 0, value: false };
  const set = {};
  let dominator = -1;

  A.forEach((item, i) => {
    equi = computeEqui(item, equi, set, i + 1);

    if (equi.value === item) dominator = i;
  });

  return equi.value === false ? -1 : dominator;
}

console.log(solution([4, 3, 4, 4, 4, 2]));
console.log(solution([-40000000000000000000000, 3, -40000000000000000000000, -40000000000000000000000, -40000000000000000000000, 3000000000000000000000]));
console.log(solution([4, 4, 2, 5, 3, 0, 4, 4]));
