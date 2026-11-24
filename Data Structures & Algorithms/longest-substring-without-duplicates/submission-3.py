class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #find the length of longest substring with no dupes
        #if there is a dupe, remove the left end til there is no more dupes
        #adjust the window from the left accordingly



        l = 0
        seen = set()
        res = 0

        "abcabcbb"
        "pwwkew"

        for r in range(len(s)):
            while s[r] in seen: #if the new char is in the set, start popping from the front til no dupes
                seen.remove(s[l])
                l+=1
            seen.add(s[r]) #add to seen
            res = max(res, r - l + 1)
        return res
        