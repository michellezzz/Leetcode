class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        d = dict()
        d[2] = ['a', 'b', 'c']
        d[3] = ['d', 'e', 'f']
        d[4] = ['g', 'h', 'i']
        d[5] = ['j', 'k', 'l']
        d[6] = ['m', 'n', 'o']
        d[7] = ['p', 'q', 'r', 's']
        d[8] = ['t', 'u', 'v']
        d[9] = ['w', 'x', 'y', 'z']

        result = []
        start = 0
        for i in range(0, len(digits)):
            if not '2' <= digits[i] <= '9':  # pass invalid input
                continue

            new_result = []
            if start == 0:
                new_result = d[int(digits[i])]
                start = 1
            else:
                for item1 in result:
                    for item2 in d[int(digits[i])]:
                        new_result.append(item1+item2)
            result = new_result

        return result

hi = Solution()

test_case = [
    '', '1', '12', '12345', '67', '27', ' ', '1 2', '34 dsa7ds'
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.letterCombinations(item)


# I?1??V?5??X?10??L?50??C?100??D?500??M?1000?