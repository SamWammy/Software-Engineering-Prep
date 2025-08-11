"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes=sorted([i.start for i in intervals])
        endTimes= sorted([i.end for i in intervals])
        
        start, end = 0, 0
        output=0
        count =0
        for interval in intervals: 
            if startTimes[start] < endTimes[end]: 
                start+=1
                count+=1
            else: 
                end+=1
                count-=1
            output=max(output,count)
        return output
