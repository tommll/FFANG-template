# Advanced Sorting - Divide and conquer - Live Coding

Lecturer: Mai Thanh Hiep


## 1. Counting sort

Problem: lecture slide


**Version 1: Basic Counting Sort**
```python
def countingSortV1(nums):
    if not nums: 
        return nums

    maxValue = max(nums)
    cnt = [0] * (maxValue + 1)
    for num in nums:
        cnt[num] += 1
        
    j = 0
    for val, freq in enumerate(cnt):
        for _ in range(freq):
            nums[j] = val
            j += 1
    
    return nums

print(countingSortV1([1, 2, 3, 0, 6, 0, 1, 1, 3]))
```

Complexity:

- Time: `O(N + K)` where `N` is length of the array, `K` is the maximum value of the array
- Space: `O(K)`

**Version 2: Stable Counting Sort**
- Stable (keeps order of equal elements)
- Needed for Radix Sort
- Needed when sorting objects by a key
```python
def countingSortV2(nums):
    if not nums:
        return nums

    maxValue = max(nums)
    
    # Step 1: Counting freq of each numbers
    cnt = [0] * (maxValue + 1)
    for num in nums:
        cnt[num] += 1
    
    # Step 2: Cumulative cnt array
    for i in range(1, maxValue+1):
        cnt[i] += cnt[i-1]
        
    # Step 3: Put numbers in the correct order with stability
    ans = [0] * len(nums)
    for val in reversed(nums):
        cnt[val] -= 1
        ans[cnt[val]] = val
    
    return ans

print(countingSortV2([1, 2, 3, 0, 6, 0, 1, 1, 3]))
```

Complexity:

- Time: `O(N + K)` where `N` is length of the array, `K` is the maximum value of the array
- Space: `O(N + K)`


## 2. Sort colors
Problem: https://leetcode.com/problems/sort-colors/description/

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for num in nums:
            cnt[num] += 1
    
        j = 0
        for num in range(3):
            for _ in range(cnt[num]):
                nums[j] = num
                j += 1
```
Complexity:

- Time: `O(N)` where `N` is length of the array
- Space: `O(1)`



## 3. Radix sort

Problem: lecture slide

```python
def radix_sort(nums: List[int]) -> List[int]:
    if not nums:
        return nums

    # Find the maximum number of digits in the largest number
    max_digits = count_digits(max(nums))

    # Sort by each digit, starting from the least significant digit
    for k in range(max_digits):
        nums = sort_by_digit(nums, k)

    return nums

def sort_by_digit(nums: List[int], k: int) -> List[int]:
    # Initialize count array
    count = [0] * 10

    # Count occurrences of each digit
    for num in nums:
        d = get_kth_digit(num, k)
        count[d] += 1

    # Compute cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place elements in sorted order
    sorted_nums = [0] * len(nums)
    for num in reversed(nums):
        d = get_kth_digit(num, k)
        count[d] -= 1
        sorted_nums[count[d]] = num

    return sorted_nums

def get_kth_digit(num: int, k: int) -> int:
    return (num // pow(10, k)) % 10

def count_digits(value: int) -> int:
    if value == 0: return 1
    return int(log10(value)) + 1

# Example usage
print(radix_sort([425, 253, 900, 79, 822, 267]))
```

Complexity:

- Time: `O(N * nDigit)` where `N` is length of the array, `nDigit` is the maximum number of digits in elements
- Space: `O(N)`


## 4. Count inversions

Problem: https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

**Solution 1: Brute force**
```python
class Solution:
    def inversionCount(self, nums, n):
        cntInversion = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    cntInversion += 1
        return cntInversion

```
Complexity:
- Time: `O(N^2)` where `N` is length of the array.
- Space: `O(1)`

**Solution 2: Merge Sort**
```python
class Solution:
    # return (num of inversions pairs, sortedArr)
    def mergeSort(self, arr): 
        if len(arr) <= 1:
            return 0, arr
            
        mid = len(arr) // 2
        cntLeft, sortedArrLeft = self.mergeSort(arr[:mid])
        cntRight, sortedArrRight = self.mergeSort(arr[mid:])
        cntMerged, sortedArr = self.merge(sortedArrLeft, sortedArrRight)
        return cntLeft + cntRight + cntMerged, sortedArr

    # return (num of inversions pairs, sortedArr)
    def merge(self, leftArr, rightArr):
        i = j = 0
        m, n = len(leftArr), len(rightArr)
        sortedArr = []
        cntInversion = 0
        while i < m and j < n:
            if leftArr[i] <= rightArr[j]:
                sortedArr.append(leftArr[i])
                i += 1
            else: # leftArr[i] > rightArr[j]
                sortedArr.append(rightArr[j])
                """
                pairs
                    (leftArr[i] > rightArr[j])
                    (leftArr[i+1] > rightArr[j])
                    (leftArr[i+2] > rightArr[j])
                    ....
                    (leftArr[m-1] > rightArr[j])
                """
                cntInversion += m - i 
                j += 1
            
        while i < m:
            sortedArr.append(leftArr[i])
            i += 1
            
        while j < n:
            sortedArr.append(rightArr[j])
            j += 1
            
        return cntInversion, sortedArr
                
    def inversionCount(self, nums, n):
        return self.mergeSort(nums)[0]
```
Complexity:
- Time: `O(NlogN)` where `N` is length of the array.
- Space: `O(N)`


## 5. Kth Largest Element in an Array

Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Solution: https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/1349609/python-4-solutions-minheap-maxheap-quickselect-clean-concise/



## 6.  Diameter of Binary Tree

Problem: https://leetcode.com/problems/diameter-of-binary-tree/

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]

    def dfs(self, root): # return pair of (diameter, height)
        if root == None:
            return 0, -1

        dLeft, hLeft = self.dfs(root.left)
        dRight, hRight = self.dfs(root.right)
        diameter = max(dLeft, dRight, hLeft + hRight + 2)
        height = max(hLeft, hRight) + 1
        return diameter, height
```
- Time: `O(N)`, where `N` is number of nodes in the binary tree.
- Space: `O(H)`, where `H` is the height of the binary tree.
