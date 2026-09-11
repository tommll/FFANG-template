# Bit manipulation - Live Coding Solutions

Lecturer: Truong Quy Quynh


## 1. Number of 1 Bits

Link problem: https://leetcode.com/problems/number-of-1-bits/



**Solution 1: Dependent on constraints**

```java
public class Solution {
  // you need to treat n as an unsigned value
  public int hammingWeight(int n) {
    int result = 0;
    for(int i = 0; i < 32; i++) {
      if (((n >> i) & 1) == 1) {
        result++;
      }
    }
    return result;
  }
}
```

Complexity:

- Time: `O(32) or O(1)`.
- Space: `O(1)`



**Solution 2: Independent on constraints**

```java
public class Solution {
  // you need to treat n as an unsigned value
  public int hammingWeight(int n) {
    int result = 0;
    while(n != 0) {
      if ((n & 1) == 1) {
        result++;
      }
      n = n >>> 1;
    }
    return result;
  }
}

```

Complexity:

- Time: `O(K)`, where `K` is number of bits in N.
- Space: `O(1)`



**Solution 3:**

```java
public class Solution {
  // you need to treat n as an unsigned value
  public int hammingWeight(int n) {
    int result = 0;
    while(n != 0) {
      result++;
      n = n & (n-1);
    }
    return result;
  }
}

```

Complexity:

- Time: `O(K)`, where `K` is number of 1 bits in N.
- Space: `O(1)`


## 2.  Reverse Bits

Link problem: https://leetcode.com/problems/reverse-bits/

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int left = 0, right = 31;
        while(left < right) {
            int i = getBit(n, left);
            int j = getBit(n, right);
            if (i != j) {
                n = flip(n, left);
                n = flip(n, right);
            }
            left++;
            right--;
        }
        return n;
    }
    
    public int getBit(int x, int k) {
        return (x >> k) & 1;
    }
    
    public int flip(int x, int k) {
        return x ^ (1 << k);
    }
}
```

Complexity:

- Time: `O(K)`, where `K` is number of bits in N.
- Space: O(1)



## 3.  Single Number

Problem link: https://leetcode.com/problems/single-number/

**Solution 1: Hashtable**

```java
class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for(int value: nums) {
            int count = countMap.getOrDefault(value, 0);
            countMap.put(value, count + 1);
        }
        for(int value: nums) {
            if (countMap.get(value) == 1) {
                return value;
            }
        }
        return -1;
    }
}

```

Complexity:
- Time: `O(N)` where `N` is length of `nums`.
- Space: `O(N)`


**Solution 2: Using `XOR` operator**

```java
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for(int value: nums) {
            result = result ^ value;
        }
        return result;
    }
}
```

Complexity:
- Time: `O(N)` where `N` is length of `nums`
- Space: `O(1)`


## 4. Subsets

Problem link: https://leetcode.com/problems/subsets/

**Solution 1: Recursion**

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        //generate tat ca cac subset co the
        List<Integer> subset = new ArrayList<>();
        buildSubset(0, nums, subset, result);
        return result;
    }

    public void buildSubset(int index, int[] nums, List<Integer> subset, List<List<Integer>> result) {
        if (index == nums.length) {
            result.add(new ArrayList<>(subset));
            return;
        }
        // chon so thu index vao subset
        subset.add(nums[index]);
        buildSubset(index + 1, nums, subset, result);
        subset.remove(subset.size() - 1); // backtracking
        // khong chon so thu index vao subset
        buildSubset(index  + 1, nums, subset, result);
    }
}
```

Complexity:

- Time: `O(N * 2^N)`, where `N` is length of `nums` array.
- Space: `O(N)`


**Solution 2: Bit manipulation**

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for(int x = 0; x < (1 << n); x++) {
            List<Integer> subset = new ArrayList<>();
            for(int i = 0; i < n; i++) {
                if (((x >> i) & 1) == 1) {
                    subset.add(nums[i]);
                }
            }
            result.add(subset);
        }
        return result;
    }
}
```

## 5. Subset followup

Problem link: in lecture slide

```java
class Solution {
    public static void main(String[] args) {
        int[] nums = new int[]{3, 2, 6, 2, 1000000000};
        System.out.println(candy(nums));
    }

    public static int candy(int[] nums) {
        int n = nums.length;
        int result = Integer.MAX_VALUE;
        for(int x = 0; x < (1 << n); x++) {
            //tong so keo quynh nhan duoc khi phan giai so x
            int quynhSum = 0;
            int brotherSum = 0;

            for(int i = 0; i < n; i++) {
                int bit = (x >> i) & 1;
                if (bit == 1) {
                    quynhSum += nums[i];
                } else {
                    brotherSum += nums[i];
                }
            }
            result = Math.min(result, Math.abs(quynhSum - brotherSum));
        }
        return result;
    }
}
```

Complexity:

- Time: `O(N * 2^N)`, where `N` is length of `nums`
- Space: `O(1)`

## 6. Bonus (Google interview)
Problem link: in lecture slide

```java
class Solution {
  public static void main(String[] args) {
    System.out.println(countWays());
  }

  /* 
    1 cột có tối đa 16 cách đặt quân cờ, biểu diễn ở dạng 4 bit: bit thứ i là 1 
    tương ứng với việc đặt quân cờ vào ô thứ i của cột đó. 
    VD: số 5 được biểu diễn là 0101 tương ứng ứng với đặt quân cờ ở vị trí 0 và 2.
    Như vậy với 2 cột liên tiếp được biểu diễn lần lượt là x và y, chúng không có 
    quân cờ chung hàng khi và chỉ khi x & y == 0.
  */
  public static int countWays() {
    int result = 0;
    int possibleWaysForColumn = 1 << 4;     
    for(int i = 0; i < possibleWaysForColumn; i++) { // cột 1
      for(int j = 0; j < possibleWaysForColumn; j++) { // cột 2
        for(int u = 0; u < possibleWaysForColumn; u++) { // cột 3
          for(int v = 0; v < possibleWaysForColumn; v++) { // cột 4     
            if ((i & j) == 0 && (j & u) == 0 && (u & v) == 0) { 
              result++;
            }
          }
        }
      }
    }
    return result;    
  }
}
```

Complexity:

- Time: `O(16^4) = O(1) or constant`
- Space: `O(1)`
