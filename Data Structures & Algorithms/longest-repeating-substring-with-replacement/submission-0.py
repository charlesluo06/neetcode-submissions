class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # updating the count of char[s[r]], return 0 if empty

            while (r-l+1) - max(count.values()) > k: #operation winLength - count of most frequent char
                count[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
        return res