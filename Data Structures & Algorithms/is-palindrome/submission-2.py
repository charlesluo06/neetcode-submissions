class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers
        #left and right, close in as they still match and skip over white space with alnum


        #racecar
        #alla

        #initialize
        l = 0
        r = len(s) - 1

        #skip update ptrs
        while l < r: 
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1

            #check if chars match
            if s[l].lower() != s[r].lower():
                return False
            #update ptrs if chars match
            l += 1
            r -= 1

        return True
