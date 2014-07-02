class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        current = 0
        for i in xrange(len(A)):
            if A[current] == 0:
                del A[current]
                A.insert(0, 0)
                current += 1
            elif A[current] == 2:
                del A[current]
                A.append(2)
            else:
                current += 1
        return

A = [1, 1, 2, 0, 2, 1, 2, 0]

result = Solution()
result.sortColors(A)
print A
