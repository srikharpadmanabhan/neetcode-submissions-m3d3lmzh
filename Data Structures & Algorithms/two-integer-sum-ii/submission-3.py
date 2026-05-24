class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        N = len(numbers)

        left = 0
        right = N - 1

        while left < right:
            sum_of = numbers[left] + numbers[right]
            if sum_of == target:
                return [left+1,right+1]
            elif sum_of < target:
                left += 1
            else:
                right -= 1

        return []