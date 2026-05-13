class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random

        def quicksort(left, right):
            if left >= right:
                return

            # Choose a random pivot to avoid O(n^2) worst case
            rand_idx = random.randint(left, right)
            nums[rand_idx], nums[right] = nums[right], nums[rand_idx]

            pivot = nums[right]
            # 3-way partition to handle duplicate elements efficiently
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            quicksort(left, lt - 1)
            quicksort(gt + 1, right)

        quicksort(0, len(nums) - 1)

        return nums