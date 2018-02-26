function solutiona(H) {
  let counter = 0;
  let minBlock = H[0];
  let current = 0;
  let blocks = [];

  H.forEach((b) => {
    if (b === 0) {
      minBlock = 0;
      current = 0;
      blocks = [];
      return;
    }

    if (b > current) {
      counter += 1;
      blocks.push(b);
    } else if (b < minBlock) {
      minBlock = b;
      blocks = [];
      counter += 1;
    } else if (b === minBlock) {
      blocks = [];
    } else {
      if (b !== current) {
        let n = blocks.length - 1;
        while (n >= 0) {
          if (blocks[n] <= b) {
            break;
          }
          blocks.pop();
          n -= 1;
        }
      }

      if (blocks.indexOf(b) === -1) {
        blocks.push(b);
        counter += 1;
      }
    }

    current = b;
  });

  return counter;
}

console.log(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]));
console.log(solution([8, 8, 5, 7, 9, 0, 7, 4, 8]));
console.log(solution([2, 0, 1]));
console.log(solution([8, 8]));

function binaryIndexOfa(searchElement, arr) {
  let minIndex = 0;
  let maxIndex = arr.length - 1;
  let currentIndex;
  let currentElement;

  while (minIndex <= maxIndex) {
    currentIndex = Math.floor((minIndex + maxIndex) / 2);
    currentElement = arr[currentIndex];

    if (currentElement < searchElement) {
      minIndex = currentIndex + 1;
    } else if (currentElement > searchElement) {
      maxIndex = currentIndex - 1;
    } else {
      return currentIndex;
    }
  }

  return minIndex;
}

// console.log(binaryIndexOfa(5, [1, 2, 4, 5, 7]));

function solution(H) {
  if (H.length < 1) {
    return 0;
  }
  const blocks = [];
  blocks.push(H[0]);
  let counter = 1;
  for (let i = 1; i < H.length; i += 1) {
    if (H[i] > H[i - 1]) {
      blocks.push(H[i]);
      counter += 1;
    } else if (H[i] < H[i - 1]) {
      let n = blocks.length - 1;
      while (n >= 0) {
        if (blocks[n] <= H[i]) {
          break;
        }
        blocks.pop();
        n -= 1;
      }

      if (blocks.length === 0 || blocks.indexOf(H[i]) === -1) {
        counter += 1;
        blocks.push(H[i]);
      }
    }
  }
  return counter;
}
