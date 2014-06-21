class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = 0
        j = 0
        delta = 0
        while i < m + delta and j < n:
            if A[i] > B[j]:
                A.insert(i, B[j])
                j += 1
                delta += 1
            i += 1
        while j < n:
            A.insert(i, B[j]) # not append T_T
            j += 1
            i += 1
        return

a = [1, 2, 3, 5, 6, 8, 10]
b = [4, 7, 9]

#a = []
#b = [1]

result = Solution()
result.merge(a, len(a), b, len(b))
print a
