class Solution(object):
    def search(self, nums, target):
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1
        # or
        low = 0
        high = len(nums)-1 
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <=nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

        