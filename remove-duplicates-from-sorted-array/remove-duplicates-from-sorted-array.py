class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in set(nums):
            counter = nums.count(i)
            while counter > 1:
                nums.remove(i)
                counter -= 1
        return len(nums)
             