class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: string
        #output: length of longest substring
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet: #case for dupe
                charSet.remove(s[l]) #remove the left most char
                l+=1 #update left til no dupe
            charSet.add(s[r]) #add to charset to know dupes
            res = max(res, r - l + 1) #update max window size
        return res