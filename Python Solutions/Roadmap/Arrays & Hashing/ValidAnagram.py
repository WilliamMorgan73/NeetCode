class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return Counter(s) == Counter(t)

        # Base case, ensure both same length

        if len(s) != len(t):
            return False
        
        d = {}
        
        # Hashmap s

        for char in s:
            if char in d: # does d.keys() by default
                # Increase value by 1
                d[char] += 1
            else:
                # Add it to dict
                d[char] = 1

        # Now loop over t

        for char in t:
            if char not in d:
                return False
            
            d[char] -=1

            if d[char] < 0:
                return False

        return True