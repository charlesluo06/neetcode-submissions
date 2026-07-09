class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]: # if valid char and if counts match
                have += 1
            
            while have==need: # match case
                if (r-l + 1) < resLen: #while window is smallest we have seen
                    res = [l,r] #update result
                    resLen = (r - l + 1) #update smallest length
                window[s[l]] -= 1 # pop from left
                if s[l] in countT and window[s[l]] < countT[s[l]]: # if the char we popped affects the match count
                    have -= 1 # deincrement try to find another valid window to end up back at match case
                l += 1 # move left ptr
        l, r = res

        return s[l : r + 1] if resLen != float("infinity") else ""



        