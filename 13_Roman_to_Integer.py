class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        last = 0
        this = 0
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'M':
                this = 1000
            elif s[i] == 'D':
                this = 500
            elif s[i] == 'C':
                this = 100
            elif s[i] == 'L':
                this = 50
            elif s[i] == 'X':
                this = 10
            elif s[i] == 'V':
                this = 5
            elif s[i] == 'I':
                this = 1
            if this < last:
                result -= this
            else:
                result += this
            last = this
        return result


hi = Solution()

test_case = [
    'I', 'IV', 'V', 'VI', 'IX', 'X', 'MCDXXXVII', 'MMMCMXCIX'

]  # common

for item in test_case:
    print "Input:", item, " output:", hi.romanToInt(item)


# I?1??V?5??X?10??L?50??C?100??D?500??M?1000?
