from typing import List
from math import ceil
MAX = 100

class peakFinder:
    def findPeakElement(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while (L < R):
            m = (L+R+1) // 2
            if nums[m - 1] > nums[m]:
                R = m - 1
            else:
                L = m
        return L, nums[L]
    
    def findMax(self, arr, rows, mid, max): # Could have used findPeakElement for this, but its flawed in 2D approach
        max_index = 0
        for i in range(rows):
            if (max < arr[i][mid]):
                max = arr[i][mid]
                max_index = i
        return max, max_index
        

    def findPeak2D(self, arr, rows, cols, mid):
        max = 0
        max, max_index = peakFinder.findMax(self, arr, rows, mid, max)

        if (mid == 0 or mid == cols - 1): 
            return max, mid, max_index

        if (max >= arr[max_index][mid - 1] and max >= arr[max_index][mid + 1]): 
            return max, mid, max_index
        
        if (max < arr[max_index][mid - 1]): 
            return peakFinder.findPeak2D(self, arr, rows, cols, mid - ceil(mid / 2.0)), mid, max_index

        if (max < arr[max_index][mid+1]):
            return peakFinder.findPeak2D(self, arr, rows, cols, mid + ceil(mid / 2.0)), mid, max_index

    
    def findPeak(self, arr):
        rows = cols = len(arr)
        mid = cols // 2
        return peakFinder.findPeak2D(self, arr, rows, cols, mid)

if __name__ == "__main__":
    peak = peakFinder()

    nums = [1,2,3,1]
    
    index, value = peak.findPeakElement(nums) 
    
    print("Array: ", nums, "\nIndex: ", index, ", Peak: ", value)   

    arr = [ [ 10, 8, 10, 10 ], 
        [ 14, 13, 12, 11 ], 
        [ 15, 9, 11, 21 ], 
        [ 16, 17, 19, 20 ] ]

    peak2D, cols, rows = peak.findPeak(arr)

    print("Array: ", arr[0], "\n       ", arr[1], "\n       ", arr[2], "\n       ", arr[3])
    print("Index: (",rows-1, cols-1,"), Peak: ", peak2D[0])
    

    