class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) > 2:
            x1,y1 = coordinates[0]
            x2,y2 = coordinates[1]
            if len(set([coordinates[i][0] for i in range(len(coordinates))])) == 1:
                return True
            if x2 - x1 !=0:
                m = (y2-y1)/(x2-x1)
                for  x,y in coordinates[2:]:
                    if y == m*(x-x1) + y1:
                        pass
                    else:
                        return False
            else:
                return False
        else:
            return True
        return True