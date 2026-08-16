class Solution(object):
    def twoSum(self, nums, target):

        n = len(nums)

        # Brute Force
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         if(nums[i]+nums[j]==target):
        #             return i,j


        # Optimal
        freq = { }
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in freq:
                return [freq[remaining],i]
            freq[nums[i]] = i