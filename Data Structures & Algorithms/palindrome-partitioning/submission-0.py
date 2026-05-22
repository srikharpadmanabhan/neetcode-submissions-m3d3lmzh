class Solution:

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        path = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(start: int):
            # If we used the whole string, save one valid partition
            if start == len(s):
                res.append(path.copy())
                return

            # Try every substring starting at `start`
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    # choose substring s[start:end+1]
                    path.append(s[start:end + 1])

                    # recurse on the rest of the string
                    helper(end + 1)

                    # undo choice
                    path.pop()

        helper(0)
        return res
                    