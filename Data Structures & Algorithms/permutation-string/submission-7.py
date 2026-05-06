class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        N, M = len(s1), len(s2)
        if N > M:
            return False

        target_dict = defaultdict(int)

        for c in s1:
            target_dict[c] += 1
        
        start = 0

        check_dict = defaultdict(int)

        for i in range(N):
            check_dict[s2[i]] += 1

        idx = N
        start 
        while idx < M:
            print(check_dict, target_dict)
            print("______________________")
            if check_dict == target_dict:
                return True
            
            check_dict[s2[start]] -= 1
            if check_dict[s2[start]] == 0:
                del check_dict[s2[start]]
            check_dict[s2[idx]] += 1
            idx += 1
            start += 1

        return check_dict == target_dict