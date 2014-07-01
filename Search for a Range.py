class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        start = 0
        end = len(A) - 1
        index1 = -1
        index2 = -1

        while start <= end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                if mid > start and A[mid - 1] == target:
                    end = mid - 1
                    continue
                index1 = mid
                break
            elif A[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1

        if index1 == -1:
            return [-1, -1]

        start = index1
        end = len(A) - 1

        while start <= end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                if mid < end and A[mid + 1] == target:
                    start = mid + 1
                    continue
                index2 = mid
                break
            elif A[mid] == target:
                start = mid + 1
            else:
                end = mid - 1

        return [index1, index2]

A = [5, 7, 7, 8, 8, 10]
A = [8, 8]
A = []
target = 8

result = Solution()
print result.searchRange(A, target)
