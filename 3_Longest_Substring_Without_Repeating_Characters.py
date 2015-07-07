class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        d = dict()
        start = 0
        max = 0
        for i in range(0, len(s)):

            #print "interation:", i, "letter", s[i]
            if s[i] in d:
                new_start = d[s[i]] + 1
                for j in range(start, d[s[i]]+1):
                    del d[s[j]]
                  #  print "delete d[%s]" % s[j]
                start = new_start
            d[s[i]] = i
            #print "add d[%s] = %d" % (s[i], i)
            if len(d)>max:
                max = len(d)
        return max

hi = Solution()

test_case = [
    '',
    'a',
    'aa',
    'aaa',
    'abcabcabc',
    'absabcabcdasgvsad',
    ''
]  # common

for item in test_case:
    print "\nInput:", item
    print "Output:\n", hi.lengthOfLongestSubstring(item)





