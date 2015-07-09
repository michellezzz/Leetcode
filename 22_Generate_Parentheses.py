class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return []

        result = [['(', 1]]   #  [exp, count(num of left - num of right)]
        for i in range(1, 2*n):
            new_result = []
            for item in result:
                exp = item[0]
                count = item[1]
                if count > 0:
                    new_result.append([exp + ')', count - 1])
                if 2*n - i > count:
                    new_result.append([exp + '(', count + 1])
            result = new_result

        final = []
        for item in result:
            final.append(item[0])
        return final


hi = Solution()

test_case = [
    0, 1, 2, 3, 5
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.generateParenthesis(item)




