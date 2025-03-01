class Solution:
    def groupAnagrams(self, strs):
        dd = dict()
        for elem in strs:
            key = ''.join(sorted(elem))
            if dd.get(key, 0):
                dd[key].append(elem)
            else:
                dd[key] = [elem]
        
        return [dd[kk] for kk in dd]


# rr = ["eat","tea","tan","ate","nat","bat"]
# print(Solution().groupAnagrams(rr))

# rr = [""]
# print(Solution().groupAnagrams(rr))
