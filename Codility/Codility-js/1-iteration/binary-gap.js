'use strict';

function binaryGap(N){
    var gate = false,
        count = 0,
        gaps = [],
        arr  = (N >>> 0).toString(2);

    for (var i = 0; i < arr.length; i++){
        if (gate) count++;

        if (arr[i] == 1 && arr[i + 1] == 0){
            gate = true;
            count = 0;
        }

        if (gate && arr[i + 1] == 1){
            gate = false;
            gaps.push(count);
        }
    }
    return (gaps.length === 0) ? 0 : Math.max.apply(null, gaps);
}

console.log(binaryGap(9));
console.log(binaryGap(529));
console.log(binaryGap(15));