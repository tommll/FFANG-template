# Stack and Queue (advanced) - Live Coding Solutions

Lecturer: Truong Quy Quynh


## 1. skyline problem

Link problem: lecture slide

**Solution 1: brute-force**

```java
public class Solution {
  public static List<Integer> skyline(int[] nums) {
    int n = nums.length;
    List<Integer> result = new ArrayList<>();
    for(int i = 0; i < n; i++) {
      int j = i - 1;
      while(j >= 0 && nums[j] <= nums[i]) {
        j--;
      }
      result.add(j);
    }
    return result;
  }
}

```

Complexity:

- Time: `O(N^2)` where `N` is length of the array.
- Space: `O(1)`



**Solution 2: Using stack**

```java
public static List<Integer> skylineStack(int[] nums) {
  int n = nums.length;
  List<Integer> result = new ArrayList<>();
  // khoi tao stack cho chi so cac phan tu
  Deque<Integer> stack = new LinkedList<>();
  for (int i = 0; i < n; i++) {
    // loai bo cac phan tu j neu nums[j] <= nums[i]
    while (!stack.isEmpty() && nums[stack.peekLast()] <= nums[i]) {
      stack.removeLast();
    }
    // ket nap ket qua cho i
    int next = stack.isEmpty() ? -1 : stack.peekLast();
    result.add(next);
    // Nem i vao stack
    stack.addLast(i);
  }
  return result;
}
```

Complexity:

- Time: `O(N)` where `N` is length of the array.
- Space: `O(N)`



## 2.   Next Greater Element II

Link problem: https://leetcode.com/problems/next-greater-element-ii/

```java
// Nhân đôi dãy và thực hiện như bài toán skyline 
// chạy vòng lặp for từ cuối về đầu.
public int[] nextGreaterElements(int[] nums) {
  int n = nums.length;
  int[] list = new int[2 * n];
  System.arraycopy(nums, 0, list, 0, n);
  System.arraycopy(nums, 0, list, n, n);
  Deque<Integer> stack = new LinkedList<>();
  int[] result = new int[n];
  for(int i = 2 * n - 1; i >=0; i--) {
    while(!stack.isEmpty() && stack.peekLast() <= list[i]) {
      stack.removeLast();
    }

    int next = stack.isEmpty() ? -1 : stack.peekLast();
    if (i < n) {
      result[i] = next;
    }

    stack.addLast(list[i]);
  }
  return result;
}


```

Complexity:

- Time: `O(N)` where `N` is length of the array.
- Space: `O(N)`



## 3.   Maximum Score of a Good Subarray

Problem link: https://leetcode.com/problems/maximum-score-of-a-good-subarray/

```java
class Solution {
  public int maximumScore(int[] nums, int k) {
    int n = nums.length;
    //left[i] la chi so cua phan tu gan i nhat ben trai ma nums[left[i]] < nums[i]
    int[] left = new int[n];
    Arrays.fill(left, -1);
    Deque<Integer> stack  = new LinkedList<>();
    for(int i = 0; i < n; i++) {
      while(!stack.isEmpty() && nums[stack.peekLast()] >= nums[i]) {
        stack.removeLast();
      }
      if (!stack.isEmpty()) {
        left[i] = stack.peekLast();
      }
      stack.addLast(i);
    }
    //right[i] la chi so cua phan tu gan i nhat ben phai ma nums[right[i]] < nums[i]
    int[] right = new int[n];
    Arrays.fill(right, n);
    stack = new LinkedList<>();
    for(int i = n-1; i >= 0; i--) {
      while(!stack.isEmpty() && nums[stack.peekLast()] >= nums[i]) {
        stack.removeLast();
      }
      if (!stack.isEmpty()) {
        right[i] = stack.peekLast();
      }
      stack.addLast(i);
    }
    //doan lien tiep tu [left[i]+1 ---> right[i] - 1] se la doan dai nhat chua nums[i] va nhan nums[i] la min
    int result = 0;
    for(int i =0; i < n; i++) {
      if (k > left[i] && k < right[i]) {
        result = Math.max(result, nums[i] * (right[i] - left[i] - 1));
      }
    }
    return result;
  }
}

```

Complexity:
- Time: `O(N)` where `N` is length of the array.
- Space: `O(N)`

## 4. Queue with Max API

Problem link: lecture slide

**Solution 1: brute-force**

```java
class MaxQueue {
  Deque<Integer> entryQueue = new LinkedList<>();
  //O(1)
  public void enqueue(int x) {
    entryQueue.addLast(x); //push vao cuoi queue
  }
  //O(1)
  public int dequeue() {
    return entryQueue.removeFirst(); //pop khoi dau queue
  }
  //O(N)
  public int getMax() {
    int result = Integer.MIN_VALUE;
    for (int value : entryQueue) {
      result = Math.max(result, value);
    }
    return result;
  }
}
```

Complexity:

- Time:
  - enqueue(): O(1)
  - dequeue(): O(1)
  - getMax(): O(N)
- Space: `O(N)`


**Solution 2: using an extra queue**

```java
class MaxQueue {
  Deque<Integer> entryQueue = new LinkedList<>();
  Deque<Integer> candidateQueue = new LinkedList<>();
  
  public void enqueue(int x) {
    entryQueue.addLast(x); 

    while(!candidateQueue.isEmpty() && candidateQueue.peekLast() < x) {
      candidateQueue.removeLast();
    }
    candidateQueue.addLast(x);
  }
  
  public int dequeue() {
    int removedValue =  entryQueue.removeFirst();
    if (!candidateQueue.isEmpty() && removedValue == candidateQueue.peekFirst()) {
      candidateQueue.removeFirst();
    }
    return removedValue;
  }
  
  public int getMax(){
    return candidateQueue.peekFirst();
  }
}
```

- Time:
    - enqueue(): Worst case is O(N) but average is O(1)
    - dequeue(): O(1)
    - getMax(): O(1)
- Space: `O(N)`

## 5.  Sliding Window Maximum

Problem link: https://leetcode.com/problems/sliding-window-maximum/

```java
class Solution {
  public Deque<Integer> candidates = new LinkedList<>();

  public int[] maxSlidingWindow(int[] nums, int k) {
    int n = nums.length;
    //tao queue chua k phan tu dau tien
    for(int i = 0; i < k; i++) {
      enqueue(nums[i]);
    }
    //move window + tinh max
    int[] result = new int[n - k + 1];
    for(int i = k; i < n; i++) {
      result[i - k] = getMax();
      //move window sang phai 1 don vi
      dequeue(nums[i - k]);
      enqueue(nums[i]);
    }
    result[n - k] = getMax();
    return result;
  }

  public void enqueue(int x) {
    while(!candidates.isEmpty() && candidates.peekLast() <x) {
      candidates.removeLast();
    }
    candidates.addLast(x);
  }

  public void dequeue(int removedValue) {
    if (removedValue == candidates.peekFirst()) {
      candidates.removeFirst();
    }
  }

  public int getMax() {
    return candidates.peekFirst();
  }
}
```
Complexity:

- Time: `O(N)`, where `N` is length of `nums`
- Space: `O(N)`

## 6.  Arithmetic expression problem

Problem link: lecture slide
```java
class Solution {
  public static Integer calculate(String[] input) {
    Deque<String> stack = new LinkedList<>();
    for(String x: input) {
      if ("+".equals(x) || "-".equals(x) || "*".equals(x)) { // neu x la phep tinh 
        stack.addLast(x);
      } else { // neu x la so
        String operation = stack.peekLast();
        if ("*".equals(operation)) {
          stack.removeLast(); //pop toan tu ra khoi stack
          Integer y = Integer.parseInt(stack.removeLast());
          Integer tempResult = y * Integer.parseInt(x);
          stack.addLast(""+tempResult);
        } else {
          stack.addLast(x);
        }
      }
    }
    //gio stack chi con chua toan hang va cac toan tu ko uu tien
    //nen chi can tinh toan tu trai qua phai
    Integer result = Integer.parseInt(stack.removeFirst());
    while(!stack.isEmpty()) {
      String operator = stack.removeFirst();
      Integer y = Integer.parseInt(stack.removeFirst());
      if ("+".equals(operator)) {
        result+=y;
      } else {
        result -=y;
      }
    }
    return result;
  }
}
```
- Time: `O(N)`, where `N` is length of `input`
- Space: `O(N)`
