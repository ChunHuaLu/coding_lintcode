# lintcode 13 -- Implement strStr()
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        s_len = len(source)
        t_len = len(target)
        if t_len == 0:
            return 0
        for i in range (0, s_len ):
            if source[i] == target[0]:
                s_tmp = source[i:i+t_len]
                print(s_tmp)
                if s_tmp == target:
                    return i
        return -1