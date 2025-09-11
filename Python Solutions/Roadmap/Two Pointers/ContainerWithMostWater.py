class Solution:
    def maxArea(self, heights) -> int:
        # two pointer
        # calculate area by height of min bar * distance between
        # Keep track of min
        # Move the smallest one inwards

        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            dist = r - l
            max_area = max(height * dist, max_area)

            # Move one smaller pointer inwards

            if heights[l] < heights[r]:
                l += 1
                continue
            elif heights[l] > heights[r]:
                r -=1
                continue
            else:
                l +=1
                r-=1

        return max_area
            