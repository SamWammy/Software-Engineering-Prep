class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=""
        tCount={}
        for val in t: 
            tCount[val]= tCount.get(val,0) +1
        
        for i in range(len(s)): 
            sCount={}
            counter=0 
            temp=""
            for j in range(i,len(s)): 
                sCount[s[j]]= sCount.get(s[j],0) +1
                temp+= s[j]

                if sCount[s[j]]== tCount.get(s[j],0):
                    counter+=1

                if counter == len(tCount) and (len(temp)< len(res) or res ==""):
                    res=temp 
                     
        return res