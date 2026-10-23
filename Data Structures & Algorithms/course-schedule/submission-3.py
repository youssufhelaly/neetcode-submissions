class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        left = [0] * numCourses

        for a, b in prerequisites:
            prereq[b].append(a)
            left[a] += 1

        queue = deque()
        for i in range(numCourses):
            if left[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            for p in prereq[course]:

                left[p] -= 1
                if left[p] == 0:
                    queue.append(p)
        return left == ([0] * numCourses)


