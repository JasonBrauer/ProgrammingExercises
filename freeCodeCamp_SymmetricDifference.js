function _oneWayComparison(array0, array1) {
  let diff = [];
  for (const element of array0) {
    if (!array1.includes(element) && !diff.includes(element)) {
      diff.push(element);
    }
  }

  return diff;
}


function _symDiff(array0, array1) {
  return _oneWayComparison(array0, array1).concat(_oneWayComparison(array1, array0));
}


function sym() {
  let totalSymDiff = arguments[0];
  for (let i=0; i < arguments.length - 1; i++) {
    totalSymDiff = _symDiff(totalSymDiff, arguments[i+1])
  }

  return totalSymDiff;
}

sym([1, 2, 3], [5, 2, 1, 4]);
