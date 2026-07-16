class Solution(object):
    def permute(self, nums):
        ans = []
        def backtrac(temp):
            if len(temp)==len(nums):
                ans.append(temp[:])
                return
            
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    backtrac(temp)
                    temp.pop()
        backtrac([])
        return ans
    

        
    
        