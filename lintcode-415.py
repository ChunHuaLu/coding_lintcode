# lintcode - 415    Valid Palindrome 2019.9.18
# Step1 :using regular expression to turn given input to string without special numbers or signs
# Step2 :store reverse string
# Step3 : compare string and reverse string
import re
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        s = s.lower()
        s = re.sub(r"\W","",s)
        print(s)
        s_len = len(s)
        s_tmp = s[::-1]
        print(s_tmp)
        if s == s_tmp:
            return True
        else:
            return False