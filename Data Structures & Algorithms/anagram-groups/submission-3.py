class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            anagrams[sortedS].append(s) # create a new group if empty and append the string there, if groups exists it'll add on to the current anagram group
        return list(anagrams.values())