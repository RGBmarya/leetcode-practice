import heapq
from collections import deque
"""
Match
Maxheap + queue

Plan
- intuition: complete most frequent tasks first to avoid unnecessary idle time (can substutite idle time with other tasks)
- hashmap to count frequency of each task
- each task becomes a node in a maxheap
- keeping track of time (start at 0):
    - increment time
    - pop root node of maxheap
    - decrement frq by 1 
    - add (task, time + n) to a queue IF frq > 0
    - if time == time + n of node on queue, add node back to maxheap
- return total time

Evaluate
Time: O(n + n + n*log(26)) -> O(n)
Space: O(n + n + n) -> O(n)
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = 1 + counts.get(task, 0)
        
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if maxHeap:
                cur_task_frq = heapq.heappop(maxHeap)
                cur_task_frq += 1
                if cur_task_frq:
                    q.append([cur_task_frq, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
            