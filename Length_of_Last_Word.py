class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        tmp = s.split()
        if len(tmp) == 0:
            return 0
        else:
            return len(tmp[-1])

hi = Solution()
print hi.lengthOfLastWord("  ")


