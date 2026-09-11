# Binary Search (ADVANCED) - Live Coding Solutions

Speaker: Mai Thanh Hiep

## 1. Binary Search - Basic

Link problem: https://leetcode.com/problems/binary-search/

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:  # Found target -> Return index
                return mid
            elif nums[mid] > target:  # Target are in the left side
                right = mid - 1
            else:
                left = mid + 1  # Target are in the right side
        return -1
```

Complexity:

- Time: `O(logN)`, where `N` is length of `nums` array.
- Space: `O(1)`



## 2. Binary Search - lower_bound

```python
def lowerBound(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            ans = mid  # update the best result so far
            right = mid - 1  # search better result on the left side
        else:
            left = mid + 1  # search result on the right side
    return ans
```

Complexity:

- Time: `O(logN)`, where `N` is length of `nums` array.
- Space: `O(1)`



## 3. Binary Search - upper_bound

```python
def upperBound(nums, target):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:  
            ans = mid  # update the best result so far
            right = mid - 1  # search better result on the left side
        else:
            left = mid + 1  # search result on the right side
    return ans
```

Complexity:

- Time: `O(logN)`, where `N` is length of `nums` array.
- Space: `O(1)`



## 4. Find First and Last Position of Element in Sorted Array (Optional Basic Course)

Problem link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1 2 4 4 7, target = 4
        # bisect_left(arr, 4) = 2
        # bisect_left(arr, 3) = 2
        # bisect_left(arr, 0) = 0
        # bisect_left(arr, 8) = 5
        idxLeft = bisect_left(nums, target)
        if idxLeft == len(nums) or nums[idxLeft] != target:
            return [-1, -1]
        
        
        # 1 2 4 4 7, target = 4
        # bisect_right(arr, 4) = 4
        # bisect_right(arr, 3) = 2
        # bisect_right(arr, 0) = 0
        # bisect_right(arr, 8) = 5
        idxRight = bisect_right(nums, target)
        return [idxLeft, idxRight - 1]
```

Complexity:

- Time: `O(logN)`, where `N` is length of `nums` array.
- Space: `O(1)`


## 5. Frequency of the Most Frequent Element

Problem link: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def getSum(left, right):
            return preSum[right+1] - preSum[left]

        def searchSmallestIndexEnoughOperations(i):
            left = 0
            right = i
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                cntOperationNeeded = nums[i] * (i-mid+1) - getSum(mid, i)
                if cntOperationNeeded <= k:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans


        nums.sort()
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
            
        ans = 0
        for i in range(n):
            j = searchSmallestIndexEnoughOperations(i)
            ans = max(ans, i - j + 1)
        return ans
```

Complexity:

- Time: `O(NlogN)`, where `N` is length of `nums` array.
- Space: `O(N)`



## 6. Minimum Number of Days to Make m Bouquets

Problem link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def calcBouquets(atDay):
            cntBouquet = 0
            cntConsecutiveFlowers = 0
            for d in bloomDay:
                if d <= atDay:
                    cntConsecutiveFlowers += 1
                else:
                    cntBouquet += cntConsecutiveFlowers // k
                    cntConsecutiveFlowers = 0

            cntBouquet += cntConsecutiveFlowers // k
            return cntBouquet


        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if calcBouquets(mid) >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
```

Complexity:

- Time: `O(log(MAX) * N)`, where `N` is length of bloomDay
- Space: `O(1)`


## 7. Longest Increasing Subsequence

Problem link: https://leetcode.com/problems/longest-increasing-subsequence

Solution link: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/


## 8. Russian Doll Envelopes
Problem link: https://leetcode.com/problems/russian-doll-envelopes/


```python
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                idx = bisect.bisect_left(sub, num)
                sub[idx] = num
        return len(sub)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort in increasing by width, if equal width sort decreasing by height
        envelopes.sort(key=lambda x:[x[0], -x[1]])
        
        arr = [h for _, h in envelopes]
        return self.lengthOfLIS(arr)
```
Complexity:

- Time: `O(NlogN)`, where `N` is the length of `envelopes`.
- Space: `O(N)`
