class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums) - 1
        output = []

        for i in range(n):

            # Avoid duplicates - Since sorted we can just check if i == i-1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicate l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicate r
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return output
