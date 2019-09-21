class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        str_rev = s[::-1]       # reverse string here
        longest = ""
        s_sum = ""
        for i in range(0, len(s)):
            for j in range(i , len(s)+1):
                sub_str = str_rev[i:j] in s            # compare substring and string
                if sub_str == True:
                    s_sum = str_rev[i:j]
            if len(s_sum) > len(longest):              # find longest palindrome
                longest = s_sum
        return longest