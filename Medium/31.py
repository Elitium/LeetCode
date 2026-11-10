# very happy with this, fully come up with the logic and implementation

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # decreasing order, check largest decreasing subsequence at end 
        # check if same length as original, then just sort
        # otherwise, swap smallest digit that is outside of subsequence with smallest in sequence that is larger and sort the remaining, guaranteed to be reverse so just flip indices (2 pointers)

        j = len(nums) - 1 # first index of subseq
        k = len(nums) - 1 # final index of subseq

        prev = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= prev:
                j = i
                prev = nums[i]
            else:
                break
        
        if k-j+1 == len(nums):
            nums.sort()
        else:
            for i in range(k, j - 1, -1):
                if nums[i] > nums[j-1]:
                    nums[j-1], nums[i] = nums[i], nums[j-1]
                    break

            while j < k:
                store = nums[k]
                nums[k] = nums[j]
                nums[j] = store
                j += 1
                k -= 1
            
