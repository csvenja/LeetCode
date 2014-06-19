# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        n = len(points)
        if n < 3:
            return n
        result = -1
        for i in xrange(n):
            slope = {'INF': 0}
            duplicate = 1
            for j in xrange(n):
                if i == j:
                    continue
                if points[i].x == points[j].x:
                    if points[i].y == points[j].y:
                        duplicate += 1
                    else:
                        slope['INF'] += 1
                else:
                    k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    if k in slope:
                        slope[k] += 1
                    else:
                        slope[k] = 1
            result = max(result, max(slope.values()) + duplicate)
        return result

a = Point(0, 0)
b = Point(1, 1)
c = Point(2, 2)
d = Point(3, 3)
points = [a, b, c, d]
result = Solution()
print result.maxPoints(points)
