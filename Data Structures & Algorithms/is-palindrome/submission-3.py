class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two ptrs l, r
        #close in as long as they match
        #skip over whitespaces
        l = 0
        r = len(s) - 1

        #racecar
        #alla


        while l < r:
            while l < r and not s[l].isalnum(): #skip whitespaces case
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False #check if chars match
            l+=1
            r-=1
        return True

        