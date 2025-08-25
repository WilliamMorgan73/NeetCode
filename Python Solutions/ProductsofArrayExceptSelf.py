from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums):
        # Put into a hash map, and search for the count of itself, -1, and then get the count of each other one and do y^x

        # Create dict containing number count

        counts = defaultdict(int)

        output = []
        for num in nums:
            # use defaultdict as key doesn't need to exist
            counts[num] += 1

        # So now dict is created, we can go through each element of the list, remove one from value and then do the rest
        # Order matters
        
        for num in nums:
            temp = 1
            counts[num] -= 1
            # Get all key value pairs
            for key, value in counts.items():
                
                temp *= key**value 

            # Append to output
            output.append(temp)
            counts[num] += 1
            
        return output
    
    def productExceptSelf2(self, nums):

        product_nonzero = 1
        zero_count = 0

        # First pass: product of nonzeros + zero count
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product_nonzero *= num

        # Second pass: build result
        output = []
        for num in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if num == 0:
                    output.append(product_nonzero)
                else:
                    output.append(0)
            else:  # zero_count == 0
                output.append(product_nonzero // num)

        return output
    
    def productExceptSelfPrefixSuffix(self, nums):
        
        # Done by AI

        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        output = [1] * n

        # Build prefix
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Build result
        for i in range(n):
            output[i] = prefix[i] * suffix[i]

        return output