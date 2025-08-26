class Solution:
    def twoSum(self, nums, target):

        d = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in d:
                return [d[difference], i]
            d[num] = i
