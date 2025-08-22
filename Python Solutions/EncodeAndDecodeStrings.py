class Solution:

    def encode(self, strs):
        
        # Create a list storing the lengths

        encoded = ""

        for st in strs:
            encoded += str(len(st)) + "#" + st

        return encoded

    def decode(self, s):
        decoded = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1

            j = i + length

            decoded.append(s[i:j])
            i = j

        return decoded