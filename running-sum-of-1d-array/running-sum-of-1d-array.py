class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.sum = 0
        self.result = []
        for i in nums:
            self.sum += i
            self.result.append(self.sum)
        return self.result
            