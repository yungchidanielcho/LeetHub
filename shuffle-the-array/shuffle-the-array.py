class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        x = nums[:n]
        y = nums[n:]
        result = []
        for i,j in zip(x,y):
            result.extend((i,j))
        return result