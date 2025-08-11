from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Base case Empty
        if len(strs) == 0:
            return [[""]]
        
        output = []

        for str in strs:
            # Get hashmap of counter and add it to the list
            h = Counter(str)
#
            flag = 0

            for sublist in output:
                # Check first word of list
                if Counter(sublist[0]) == h:

                    # Add to that sublist
                    sublist.append(str)
                    flag = 1
                    break

            if flag == 0:
                output.append([str])
    
        # Return
        return output
    
    def groupAnagrams2(self, strs):
            # Dictionary: key = tuple of letter counts, value = list of anagrams
            # With a defaultdict, if the key doesn’t exist, it automatically creates it with a default value (which you specify when creating it).
            groups = defaultdict(list)

            for word in strs:
                # Step 1: Use Counter to count letters in the current word
                letter_counts = Counter(word)

                # Step 2: Create a fixed-size list of 26 zeros
                count_list = [0] * 26

                # Step 3: Fill in the counts for each letter in the right position
                for letter, freq in letter_counts.items():
                    index = ord(letter) - ord('a')  # find position 0–25
                    count_list[index] = freq

                # Step 4: Convert list to a tuple (immutable so it can be a dict key)
                count_tuple = tuple(count_list)

                # Step 5: Add the current word to the correct group
                groups[count_tuple].append(word)

            # Step 6: Return just the grouped anagrams
            return list(groups.values())