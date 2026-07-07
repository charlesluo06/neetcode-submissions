class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)): #sets up the window size for s1 and s2
            s1Count[ord(s1[i]) - ord('a')] += 1 #get ASCII value, 97 - 97 + 1 = 1, Start at 0
            s2Count[ord(s2[i]) - ord('a')] += 1 #get ASCII value

        matches = 0 #initialize matches
        for i in range(26): #iterate thru and update matches on first window
            if s1Count[i] == s2Count[i]:
                matches += 1
            else:
                matches += 0

        l = 0
        for r in range(len(s1), len(s2)): #starting after the end of s1
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a') #find our index
            s2Count[index] += 1 #increment count every time we slide
            if s1Count[index] == s2Count[index]:    #if s1 and s2 counts match while we are looking at that letter, match!
                matches +=1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -=1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches +=1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -=1
            l+=1
        return matches == 26




            