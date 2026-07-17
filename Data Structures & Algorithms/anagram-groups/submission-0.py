class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        dictionary = {}
        for string in strs:
            k = "".join(sorted(string))
            if k in dictionary:
                groups[dictionary[k]].append(string)
            else:
                groups.append([string])
                dictionary[k] = len(groups) - 1
        return groups     



        