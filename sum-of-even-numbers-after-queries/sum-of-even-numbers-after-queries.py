class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        from itertools import compress
        self.answer = []
        self.evensum = sum([v for v in A if v % 2 == 0])
        for i in range(len(queries)):
            self.val = queries[i][0]
            self.index = queries[i][1]
            
            if A[self.index] % 2 == 0:
                # Even number + Even number is even number
                if self.val % 2 == 0:
                    self.evensum += self.val
                # Even number + Odd Number is odd number
                else:
                    self.evensum -= A[self.index]
            else:
                # Odd number + Odd number is even number
                if self.val % 2 != 0:
                    self.evensum += self.val + A[self.index]
                # Odd number + even number is odd number
                else:
                    pass
            A[self.index] += self.val

            self.answer.append(self.evensum)
        
        return self.answer