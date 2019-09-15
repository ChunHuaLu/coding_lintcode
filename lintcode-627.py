# 627 Longest Palindrome
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        s_member = set(s)
        s_count = [0] * len(s_member)
        s_member = list(s_member)

        for i in range(0, len(s)):
            for j in range(0, len(s_member)):
                if s[i] == s_member[j]:
                    s_count[j] += 1
        print(s_member)
        print(s_count)
        longest = 0
        is_odd = 0
        for i in range(0, len(s_count)):
            if s_count[i] % 2 == 0:
                longest = longest + s_count[i]
            if s_count[i] % 2 == 1 and s_count[i] > 2:
                longest = longest + (s_count[i] // 2) * 2
                s_count[i] = s_count[i] % 2
        for i in range(0, len(s_count)):
            if s_count[i] % 2 == 1 and is_odd == 0:
                is_odd = 1
                longest = longest + 1
        return longest