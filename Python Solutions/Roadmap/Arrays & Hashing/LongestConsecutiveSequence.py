from collections import Counter

class Solution:
    def longestConsecutive(self, nums) -> int:
        
        current_length = 1
        max_length = 1

        # Base case, empty list
        if nums == []:
            return 0

        # Create counter

        count = Counter(nums)

        # Loop over each num in array
        for num in nums:
            # check if n-1 exists
            if num-1 in count:
                # Not start of sequence
                continue
            else:
                # Start of sequence
                # Check if n+1 exists, and then update current num and continue increasing count
                current_num = num

                while current_num + 1 in count:
                    # Increase current_length
                    current_length += 1
                    current_num += 1

                if max_length < current_length:
                    max_length = current_length

                # Reset current_length
                current_length = 1

        return max_length