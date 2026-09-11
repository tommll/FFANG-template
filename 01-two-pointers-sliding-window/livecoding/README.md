# Two Pointers - Sliding Window - Live Coding Solutions

Lecturer: Mai Thanh Hiep


## 1. Two Sum II - Input Array Is Sorted

Link problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/



**Solution 1: Brute force**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]
```

Complexity:

- Time: `O(N^2)`, where `N` is length of `nums` array.
- Space: `O(1)`



**Solution 2: HashTable**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, b in enumerate(nums):
            a = target - b
            if a in seen:
                return [seen[a]+1, i+1]
            seen[b] = i
```

Complexity:

- Time: `O(N)`, where `N` is length of `nums` array.
- Space: `O(N)`



**Solution 3: Binary Search**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        for i in range(n):
            # binary search target - nums[i], [i+1...n-1]
            res = binarySearch(nums, i+1, n-1, target - nums[i])
            if res != -1:
                return [i+1, res+1]
```

Complexity:

- Time: `O(NlogN)`, where `N` is length of `nums` array.
- Space: `O(1)`



**Solution 4: Two Pointers**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
```

Complexity:

- Time: `O(N)`, where `N` is length of `nums` array.
- Space: `O(1)`



## 2. 3Sum

Link problem: https://leetcode.com/problems/3sum/

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > 0: break  # Since arr[i] <= arr[l] <= arr[r], if arr[i] > 0 then sum=arr[i]+arr[l]+arr[r] > 0
            l = i + 1
            r = n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l+1 < n and nums[l+1] == nums[l]: l += 1  # Skip duplicates nums[l]
                    l += 1
                    r -= 1
                elif sum3 < 0: l += 1
                else: r -= 1
                
            while i+1 < n and nums[i+1] == nums[i]: i += 1  # Skip duplicates nums[i]
            i += 1
        return ans
```

Complexity:

- Time: `O(N^2)`, where `N` is length of `nums` array.
- Extra Space (without counting output as space): `O(sorting(N))`
    - Python: Timsort O(N)
    - C++: IntroSort O(logN)
    - Java: sort pritimitive types using Dual-Pivot Quicksort O(logN); sort objects using Timsort O(N)
    - HeapSort: O(1)

## 3. 3Sum Smaller

Problem link: https://leetcode.com/problems/3sum-smaller/

**Idea**
- To use Two Pointer, let's sort `nums` in increasing order first.
- Now, we need to find 3 elements so that **nums[i] + nums[j] + nums[k] < target**, `(i < j < k)`.
- We fix `nums[k]`, by iterating `k` in range `[2..n-1]`, the answer is the total number of pairs `(nums[i]`, `nums[j])` for each `nums[k]`, `(i < j < k)`, so that `nums[i] + nums[j] < target - nums[k]`.
	- We start with` i = 0`, `j = k - 1`
	- If `nums[i] + nums[j] < target - nums[k]` then:
		-  There are `j-i` valid pairs, because in that case, when `nums[k]` and `nums[i]` are fixed, moving `j` to the left side always causes `nums[i] + nums[j] < target - nums[k]`.
		-  Try another `nums[i]` by increasing `i` by one, so `i += 1`.
	- Else if `nums[i] + nums[j] >= target - nums[k]` then:
		- Because `nums[k]` is fixed, to make the inequality correct, we need to decrease sum of `nums[i] + nums[j]`.
		- There is only one choice is to decrease `nums[j]`, so `j -= 1`.

![image](https://assets.leetcode.com/users/images/d267f4a4-7e31-4372-8bb2-a99744ac41d0_1626427125.272143.png)


```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] < target - nums[k]:
                    ans += j - i
                    i += 1
                else:
                    j -= 1
        return ans
```

**Complexity**
- Time: `O(N^2)`, where `N <= 3500` is number of elements in the array `nums`.
- Space: `O(sorting(N))`.
    - Python: Timsort O(N)
    - C++: IntroSort O(logN)
    - Java: sort pritimitive types using Dual-Pivot Quicksort O(logN); sort objects using Timsort O(N)
    - HeapSort: O(1)


## 4. Minimum Size Subarray Sum

Problem link: https://leetcode.com/problems/minimum-size-subarray-sum/

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        ans = math.inf
        for r, num in enumerate(nums):
            curSum += num
            while curSum >= target:
                ans = min(ans, r - l + 1)
                curSum -= nums[l]
                l += 1
        return 0 if ans == math.inf else ans
```

Complexity:

- Time: `O(N)`, where `N` is length of `nums` array.
- Space: `O(1)`



## 5. Longest Substring Without Repeating Characters

Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Solution 1: Using Set 
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        ans = 0
        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1

            seen.add(c)
            ans = max(ans, r - l + 1)

        return ans 
```
Complexity:
- Time: `O(N)`, where `N` is length of string `s`
- Space: `O(K)`, where `K` is the number of different characters in string `s`.


Solution 2: Using Last Index
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        lastIndex = [-1] * 128
        ans = 0
        for r, c in enumerate(s):
            if lastIndex[ord(c)] >= l:
                l = lastIndex[ord(c)] + 1
            ans = max(ans, r - l + 1)
            lastIndex[ord(c)] = r
        return ans
```
Complexity:
- Time: `O(N)`, where `N` is length of string `s`
- Space: `O(1)`


## 6. Longest Substring with At Most K Distinct Characters

Problem link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        cnt = Counter()
        ans = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            
            while len(cnt) > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    cnt.pop(s[l])
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans   
```

Complexity:

- Time: `O(N)`, where `N` is length of string `s`.
- Space: `O(1)`


## 7. Find All Anagrams in a String

Problem link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Solution: https://leetcode.com/problems/find-all-anagrams-in-a-string/solutions/639309/java-python-sliding-window-detail-explanation-clean-concise/

