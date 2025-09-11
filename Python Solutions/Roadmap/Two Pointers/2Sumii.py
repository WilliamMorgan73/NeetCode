class Solution:
    def twoSum(self, numbers, target):
        # Create 2 pointers
        # If less than needed, move l out
        # If larger than needed, move r in

        l = 0
        r = len(numbers)-1

        while l <= r:
            
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
                continue
            else:
                r -= 1
                continue

        return False