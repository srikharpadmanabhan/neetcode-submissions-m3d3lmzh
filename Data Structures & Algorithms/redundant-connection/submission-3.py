class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parents = [i for i in range(len(edges)+1)]
        ranks = [1 for i in range(len(edges) + 1)]

        def find(i):
            while parents[i] != i:
                i = parents[i]
            
            return i
        
        def union(i, j):

            par1 = find(i)
            par2 = find(j)

            if par1 == par2:
                return False
            
            if ranks[par1] > ranks[par2]:
                ranks[par1] += ranks[par2]
                parents[par2] = par1
            else:
                ranks[par2] += ranks[par1]
                parents[par1] = par2

            return True
        
        for (u,v) in edges:
            if not union(u,v):
                return [u, v]
        
        return []