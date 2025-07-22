class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count ={}

        for val in s1: 
            s1Count[val]= s1Count.get(val,0) +1
        #populates s1 count with each character 
        #and how much they appear 
        
        for i in range(len(s2)):
            #loops through the contents of string s2 
            # creates a new dictionary and result for every window to find a permutation 

            s2Count={}
            res=0 
            for j in range(i,len(s2)):
                #loops through every window starting from i to len(s2)
                # meaning that the window slides to the right
                # accumulates contents of the string into a hashmap 
                # if the character in the hashmap appears more than the hashmap containing s1 
                # we can assume thats not a permutation 
                # however if it appears exactly the same amount of times, we can assume that the characters match 
                
                s2Count[s2[j]] = s2Count.get(s2[j],0) +1

                if s2Count[s2[j]] > s1Count.get(s2[j],0):
                    break

                if s2Count[s2[j]] == s1Count.get(s2[j],0):
                    res+=1
                # if statement at the very bottom 
                # res is an accumulation of matching characters 
                # once res is equal to the length of s1,
                # this means that res matches the same amount of characters as s1 
                # hence there is a permutation 
                if res == len(s1Count): 
                    return True
        return False 


        