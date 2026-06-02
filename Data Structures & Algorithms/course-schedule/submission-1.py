class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        start_courses = set([i for i in range(numCourses)])
        prereq_nums = defaultdict(int)
        prereq_dict = defaultdict(list)

        courses_taken = set()

        for course, prereq in prerequisites:
            prereq_nums[course] += 1
            prereq_dict[prereq].append(course)
        
        
        queue = deque([i for i in range(numCourses) if i not in prereq_nums])

        while queue:
            top = queue.popleft()
            if top in courses_taken:
                continue
            
            courses_taken.add(top)

            for neighbor in prereq_dict[top]:
                prereq_nums[neighbor] -= 1
                
                if prereq_nums[neighbor] == 0:
                    queue.append(neighbor)
                    
        return len(courses_taken) == numCourses

