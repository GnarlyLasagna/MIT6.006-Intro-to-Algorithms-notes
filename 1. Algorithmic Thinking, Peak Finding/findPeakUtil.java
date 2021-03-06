
class PeakElement {
	
	static int findPeakUtil(
		int arr[], int low, int high, int n)
	{
		
		int mid = low + (high - low) / 2;

		if ((mid == 0 || arr[mid - 1] <= arr[mid])
			&& (mid == n - 1 || arr[mid + 1] <= arr[mid]))
			return mid;
		// If middle element is not peak
		// and its left neighbor is
		// greater than it, then left half
		// must have peak . else the right half has peak
		else if (mid > 0 && arr[mid - 1] > arr[mid])
			return findPeakUtil(arr, low, (mid - 1), n);
		
		else
			return findPeakUtil(
				arr, (mid + 1), high, n);
	}
	static int findPeak(int arr[], int n)
	{
		return findPeakUtil(arr, 0, n - 1, n);
	}

	// Driver method
	public static void main(String[] args)
	{
		int arr[] = { 1, 3, 20, 4, 1, 0 };
		int n = arr.length;
		System.out.println(
			"Index of a peak point is " + findPeak(arr, n));
	}
}