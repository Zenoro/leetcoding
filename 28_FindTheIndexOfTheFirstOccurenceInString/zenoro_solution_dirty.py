class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1



# haystack = "leetcode"; needle = "leeto"
# print(strStr(haystack, needle))

# haystack = "sadbutsad"; needle = "sad"
# print(strStr(haystack, needle))
