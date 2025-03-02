class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def create_dict(ss):
            d1 = {}
            for elem in ss:
                if d1.get(elem, 0):
                    d1[elem] += 1
                else:
                    d1[elem] = 1
            return d1

        for i in range(len(s2)-len(s1)+1):
            wnd = s2[i:i+len(s1)]

            if create_dict(wnd) == create_dict(s1):
                return True
        return False


# s1 = "ab"; s2 = "eidbaooo"
# print(Solution().checkInclusion(s1, s2))

# s1 = "ab"; s2 = "eidboaoo"
# print(Solution().checkInclusion(s1, s2))

# s1 = "adc"; s2 = "dcda"
# print(Solution().checkInclusion(s1, s2))

s1 = "hello"; s2 = "ooolleoooleh"
print(Solution().checkInclusion(s1, s2))
