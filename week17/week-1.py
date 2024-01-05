class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 1
        table = [0]*n
        table[0] = 1
        for i in range(1,n):
            table[i]=1
            for k in range(i):
                if nums[i]>nums[k] and table[k]+1>table[i]:
                    table[i] = table[k]+1
            if table[i]>ans:ans=table[i]
        return ans