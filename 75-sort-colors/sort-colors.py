class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap the elements at mid and low
                nums[low], nums[mid] = nums[mid], nums[low]
                # Move both pointers forward
                low += 1
                mid += 1
                
            elif nums[mid] == 1:
                # 1 is in the correct middle section, just move mid forward
                mid += 1
                
            else:
                # The element is 2. Swap it to the high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                # Move the high boundary down
                high -= 1