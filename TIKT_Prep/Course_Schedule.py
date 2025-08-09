class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList={ i:[] for i in range(numCourses)}

        for course, prereq in prerequisites: 
            adjacencyList[course].append(prereq)
        
        #all visited nodes so far
        visited = set()

        def dfs(currCourse): 
            if currCourse in visited: 
                return False 
            if adjacencyList[currCourse] ==[]: 
                return True
            
            visited.add(currCourse)

            for prereqs in adjacencyList[currCourse]: 
                if not dfs(prereqs): return False # if dfs is false return false 
            visited.remove(currCourse)
            adjacencyList[currCourse]=[] # since we know that this is okay 
            return True

        for course in range(numCourses): 
            if not dfs(course): return False 
        return True
        