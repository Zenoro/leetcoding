class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        j = 0
        len_s, len_t = len(s), len(t)
        error = 0
        equal_lens = False
        match d := len_s - len_t:
            case -1:
                return self.is_one_edit_distance(t, s)
            case _ if d > 1 or d < -1:
                return False
            case 0:
                equal_lens = True
        
        for i in range(len_t):
            if error == 2:
                return False
            if t[i] == s[j]:
                j += 1
            else:
                error += 1
                if equal_lens:
                    j += 1
        return bool((not error or equal_lens) and (error or not equal_lens))

print(Solution().is_one_edit_distance('aDb', 'adb')) # True
print(Solution().is_one_edit_distance('ab', 'ab')) # False
print(Solution().is_one_edit_distance('aBcd', 'abCd')) # False
print(Solution().is_one_edit_distance('abcd', 'abc')) # True
print(Solution().is_one_edit_distance('aBcd', 'abc')) # False