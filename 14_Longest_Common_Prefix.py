class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        common = strs[0]
        for i in range(1, len(strs)):
            if common == '':
                return ''
            else:
                common = self.longestprefix(common, strs[i])
        return common

    def longestprefix(self, str1, str2):
        if str1 == '' or str2 == '':
            return ''
        if str1 == str2:
            return str1
        if str1[0] != str2[0]:
            return ''
        else:
            return str1[0] + self.longestprefix(str1[1:], str2[1:])


hi = Solution()

test_case = [
    ["12", '', '12'],
    [''],
    [],
    ["12", "123", "1234"],
    ['sdgs', 'sdg', "sdgetgwe"],
    ['21312']
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.longestCommonPrefix(item)