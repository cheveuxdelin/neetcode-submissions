class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = {i: [] for i in pid}
        result = []

        for i in range(len(ppid)):
            current = pid[i]
            parent = ppid[i]
            if parent != 0:
                d[parent].append(current)
        
        def helper(current):
            result.append(current)
            for child in d[current]:
                helper(child)
        
        if kill not in d:
            return []
        
        helper(kill)
        return result