from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        # Create a dict that stores the count of each number:
        # Can use defaultdict as will create a new key if does not exist

        count = defaultdict(int)

        # loop through each num in nums

        for num in nums:
            count[num] += 1

        # Find the k largest values and return the keys

        sortedKeys= sorted(count, key=count.get, reverse=True)

        # return the last k elemnts of sortedKeys

        return sortedKeys[:k]

    def topKFrequentBucket(self, nums, k):
        buckets = []

        # Step 1: Count frequencies
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # Make empty buckets
        
        buckets = [[] for _ in range(len(nums) + 1)]

        # Fill buckets
        # Index = frequency
        # Value = list of numbers with that frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Gather top k starting from the end
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    break
            if len(res) == k:
                break
            
        return res