class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: string
        #output: length of longest substring
        #zxyzxyz
        
        mySet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            #case where dupe
            while s[r] in mySet:
                mySet.remove(s[l])
                l+=1
            mySet.add(s[r])
            res = max(res, r - l + 1) #update res with current window width

        return res
        