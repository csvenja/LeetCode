class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n < 1:
            return False
        m = len(matrix[0])
        if m < 1:
            return False
        start = 0
        end = n - 1
        if matrix[start][0] == target or matrix[end][0] == target:
            return True
        while end - start > 1:
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        current = matrix[start]
        if matrix[end][0] < target:
            current = matrix[end]
        start = 0
        end = m - 1
        while end - start > 1:
            mid = start + (end - start) / 2
            if current[mid] == target:
                return True
            elif current[mid] < target:
                start = mid
            else:
                end = mid
        if current[start] == target or current[end] == target:
            return True
        return False

matrix = [[1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
target = 3
# matrix = []
# matrix = [[1], [3]]

result = Solution()
print result.searchMatrix(matrix, target)
