class Solution:
    def hasDuplicate(self, nums) -> bool:

        
        dict = {}

        # Loop over each number in the array, and store in hash map.
        for item in nums:
            # If item exists in dict, return True
            if item in dict.keys():
                return True
            else:
                # Add do dict
                dict[item] = 1

        # No duplicates - return False
        return False