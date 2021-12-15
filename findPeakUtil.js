function findPeakUtil(arr, low, high, n) {
  var mid = low + parseInt((high - low) / 2);

  if (
    (mid == 0 || arr[mid - 1] <= arr[mid]) &&
    (mid == n - 1 || arr[mid + 1] <= arr[mid])
  )
    return mid;
  // If middle element is not peak
  // and its left neighbor is
  // greater than it, then left half
  // must have peak . else the right half has peak
  else if (mid > 0 && arr[mid - 1] > arr[mid])
    return findPeakUtil(arr, low, mid - 1, n);
  else return findPeakUtil(arr, mid + 1, high, n);
}

function findPeak(arr, n) {
  return findPeakUtil(arr, 0, n - 1, n);
}

// Driver Code
var arr = [1, 3, 20, 4, 1, 0];
var n = arr.length;
console.log("Index of a peak point is " + findPeak(arr, n));
