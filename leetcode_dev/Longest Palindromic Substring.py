import copy

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s1, s2):
        '''
        if len(s) == 0:
            return 0

        reversed = s[::-1]
        '''

        last_mat = []
        mat = []


        s = s1
        reversed = s2

        for i in range(0, len(s)):  # s  string

            for j in range(0, len(reversed)):   # reversed   string
                if s[i] == reversed[j]:
                    same = 1
                else:
                    same = 0

                if i == 0:
                    mat.append(same)
                    break
                else:
                    if j == 0:
                        mat[j] = same
                    else:
                        mat[j] = same*(last_mat[j-1]+same)
            print mat
            last_mat = copy.deepcopy(mat)
        return mat[-1]


hi = Solution()

test_case = [
    ("123", "321"),
    ("1225412", "1233312"),
    ("crux.com", "google.com"),
    ("12300123400", "12399123499")

]  # common

for item in test_case:
    print "Input:", item, " output:", hi.longestPalindrome(item[0], item[1])