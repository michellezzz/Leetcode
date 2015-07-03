class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    # Returns the index of the first occurrence of needle in haystack,
    # or -1 if needle is not part of haystack.
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
             return -1
        else:
            for i in range(0, len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1

hi = Solution()

test_case = [
    ["", ""],
    ["123", ""],
    ["123", "1234"],
    ["123423", "23"],
    ["123", "1"],
]  # common

for item in test_case:
    print "Input:", item, " output:", hi.strStr(item[0], item[1])
