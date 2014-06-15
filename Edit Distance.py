class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        insert = 1
        delete = 1
        replace = 1
        length1 = len(word1) + 1
        length2 = len(word2) + 1
        distance = [[0 for j in xrange(length2)] for i in xrange(length1)]
        for i in xrange(1, length1):
            distance[i][0] = distance[i - 1][0] + insert
        for j in xrange(1, length2):
            distance[0][j] = distance[0][j - 1] + delete
        for j in xrange(1, length2):
            for i in xrange(1, length1):
                insertCost = distance[i - 1][j] + insert
                deleteCost = distance[i][j - 1] + delete
                replaceCost = distance[i - 1][j - 1] + replace
                if word1[i - 1] == word2[j - 1]:
                    replaceCost -= replace
                distance[i][j] = min(insertCost, deleteCost, replaceCost)
        return distance[length1 - 1][length2 - 1]

word1 = "gumbo"
word2 = "gamble"

result = Solution()
print result.minDistance(word1, word2)
