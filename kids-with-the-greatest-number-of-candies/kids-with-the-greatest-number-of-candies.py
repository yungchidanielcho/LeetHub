class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        result = []
        for n in candies:
            if maxcandies - n <= extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
                