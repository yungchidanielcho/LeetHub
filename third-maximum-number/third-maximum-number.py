class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        unique = []
        while len(nums) > 0:
            var = nums.pop(0)
            if var not in unique:
                unique.append(var)
            if len(unique) == 3:
                return unique[2]
        return unique[0]
    #O(n)