class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two ptrs, closes in while the chars match
        #have to skip over white spaces while left ptr doesn't cross over right ptr
        #return true if loop goes all the way, false if no match


        #initialize ptrs
        l = 0
        r = len(s) - 1 #index based for - 1

        #racecar
        #alla

        while l < r:
            while l < r and not s[l].isalnum(): #case for white spaces on left and right side
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower(): #if no match, false ACCOUNT FOR CASE SENSITIVE
                return False
            #if checks pass update ptrs
            l+=1
            r-=1
        return True #ran thru whole phrase and is good