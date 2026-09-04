class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = sorted(nums1+nums2)
        n = len(arr)
        if n%2:
            return float(arr[n//2])
        return (arr[n//2-1]+arr[n//2])/2.0