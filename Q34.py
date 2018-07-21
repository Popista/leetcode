
class Solution(object):
    left, right = 0, 0
    def search(self,nums,i,j,target):
        m = (i + j) / 2
        if m == i:
            if nums[m] == target:
                self.left = min(self.left, m)
                self.right = max(self.right, m)
            if m + 1 == len(nums) - 1 and nums[m+1] == target:
                self.left = min(self.left, m+1)
                self.right = max(self.right, m+1)
            return
        if nums[m] < target:
            self.search(nums,m,j,target)
        elif nums[m] > target:
            self.search(nums,i,m,target)
        else:
            x = m
            while i <= x:
                if nums[x] == target:
                    self.left = min(self.left, x)
                x -= 1
            x = m

            while j >= x:
                if nums[x] == target:
                    self.right = max(self.right, x)
                x += 1
            return


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.left = len(nums) - 1
        self.search(nums,0,len(nums)-1,target)
        if self.left > self.right:
            return -1,-1
        return self.left, self.right
t = Solution()
print t.searchRange([5,5, 7, 7, 7, 8,10],10)