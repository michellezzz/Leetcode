class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):  # its better to get pattern by just sorting the word
        pattern_dict = {}
        for word in strs:
            letter_dict = {}
            for letter in word:
                if letter in letter_dict:
                    letter_dict[letter] += 1
                else:
                    letter_dict[letter] = 1
            pattern = ''
            for letter in sorted(letter_dict):
                pattern += letter + str(letter_dict[letter])
            # print "pattern:",  pattern

            if pattern in pattern_dict:
                pattern_dict[pattern].append(word)
            else:
                pattern_dict[pattern] = [word]

        # print "pattern dict:", pattern_dict
        result = []
        for pattern in pattern_dict:
            if len(pattern_dict[pattern])>1:
                result.extend(pattern_dict[pattern])
        return result


hi = Solution()

test_case = [
    ["asdf", "fdas", "erefbaw", "htrjae"]
    ]# common


for item in test_case:
    print "\n\nInput:", item, "  output", hi.anagrams(item)
