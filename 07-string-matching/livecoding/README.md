# String matching - Live Coding Solutions

Lecturer: Truong Quy Quynh

## 1. Brute force

Link problem: lecture slide

```java
public class Solution {
    public static int findMatch(String t, String p) {
        int m = t.length(), n = p.length();
        for (int i = 0; i < m - n; i++) {
            if (t.substring(i, i + n).equals(p)) {
                return i;
            }
        }
        return -1;
    }
}
```

Complexity:

- Time: `O(M * N)` where `M` is length of `T`, `N` is the length of `P`
- Space: `O(1)`

## 2. Rabin-Karp algorithm

Link problem: lecture slide
```java
// First version with bugs
class Solution {
    public static int findMatch(String t, String p) {
        int m = t.length(), n = p.length();
        // Buoc 1: Chon so K
        int k = 2;
        int power = (int) Math.pow(k, n - 1);
        // Buoc 2: Tinh hash(p) va hash cua t[0..n-1]
        int pHash = 0, tHash = 0;
        for (int i = 0; i < n; i++) {
            pHash = (pHash * k) + p.charAt(i);
            tHash = (tHash * k) + t.charAt(i);
        }
        // Buoc 3: so sanh va dich cua so
        for (int i = 0; i < m - n; i++) {
            if (pHash == tHash && p.equals(t.substring(i, i + n))) {
                return i;
            }
            // dich cua so
            if (i < m - n) {
                tHash = k * (tHash - t.charAt(i) * power) + t.charAt(i + n);
            }
        }
        return -1;
    }
}
```

```java
// fix overflow and modulor bugs
class Solution {
  public int strStr(String t, String p) {
    int m = t.length(), n = p.length();
    if (m < n) {
      return -1;
    }
    int k = 2;
    int mod = 101;
    // power = Math.pow(base, n - 1 ) % mod;
    int power = 1; 
    for(int i = 1; i < n; i++) {
      power = (power * k) % mod;
    }
    int pHash = 0, tHash = 0;
    // buoc 1: Tinh hash cua P va hash cua N ki tu dau tien cua T
    for(int i = 0; i < n; i++) {
      pHash = (pHash * k + p.charAt(i)) % mod;
      tHash = (tHash * k + t.charAt(i)) % mod;
    }
    // Buoc 2: dich cua so va so sanh
    for(int i = 0; i <= m - n; i++) {
      if (pHash == tHash && p.equals(t.substring(i, i + n))) {
        return i;
      }
      if (i < m - n) {
        tHash = (k *(tHash - t.charAt(i) * power) + t.charAt(i+n)) %  mod;
        if (tHash < 0) {
          tHash += mod;
        }
      }
    }
    return -1;
  }
}

```

Complexity:

- Time: `O(M + N)` where `M` is length of string `T` and `N` is the length of string `p`
- Space: `O(1)`

## 3. Find the Index of the First Occurrence in a String

Link problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

```java
class Solution {
  public int strStr(String t, String p) {
    int m = t.length(), n = p.length();
    if (m < n) {
      return -1;
    }
    int base = 2;
    int mod = 101;
    // power = Math.pow(base, n - 1 ) % mod;
    int power = 1; 
    for(int i = 1; i < n; i++) {
      power = (power * base) % mod;
    }
    int pHash = 0, tHash = 0;
    // buoc 1: Tinh hash cua P va hash cua N ki tu dau tien cua T
    for(int i = 0; i < n; i++) {
      pHash = (pHash * base + p.charAt(i)) % mod;
      tHash = (tHash * base + t.charAt(i)) % mod;
    }
    // Buoc 2: dich cua so va so sanh
    for(int i = 0; i <= m - n; i++) {
      if (pHash == tHash && p.equals(t.substring(i, i + n))) {
        return i;
      }
      if (i < m - n) {
        tHash = (base *(tHash - t.charAt(i) * power) + t.charAt(i+n)) %  mod;
        if (tHash < 0) {
          tHash += mod;
        }
      }
    }
    return -1;
  }
}
```

- Time: `O(M + N)` where `M` is length of string `T` and `N` is the length of string `p`
- Space: `O(1)`

## 4. Permutation in string

Link problem: https://leetcode.com/problems/permutation-in-string/

```java
/**
 * Solution: Ánh xạ kí tự a -> 1, b -> 2, c-> 4, d -> 8. Tổng quát kí tự ch -> 2 ^ (ch-'a'). 
 * Giá trị hash của string ở đây được tính bẳng tổng các ánh xạ của các kí tự trong string.
 */
class Solution {
  public boolean checkInclusion(String p, String t) {
    int m = t.length(), n = p.length();
    if (m < n) {
      return false;
    }
    int pHash = 0, tHash = 0;
    for(int i = 0; i < n; i++) {
      pHash = pHash + getHash(p.charAt(i));
      tHash = tHash + getHash(t.charAt(i));
    }
    for(int i = 0; i <= m - n; i++) {
      if (tHash == pHash && isPermutation(p, t.substring(i, i + n))) {
        return true;
      }
      if (i < m - n) {
        tHash = tHash - getHash(t.charAt(i)) + getHash(t.charAt(i + n));    
      }      
    }
    return false;
  }

  public int getHash(char ch) {
    return 1 << (ch - 'a');
  }

  public boolean isPermutation(String a, String b) {
    char[] arrA = a.toCharArray();
    char[] arrB = b.toCharArray();
    Arrays.sort(arrA);
    Arrays.sort(arrB);
    return new String(arrA).equals(new String(arrB));
  }
}
```

Complexity:

- Time: `O(M)` where `M` is length of string `T`
- Space: `O(1)`

## 5. Implement Trie (Prefix Tree)

Problem link: https://leetcode.com/problems/implement-trie-prefix-tree/

**Solution: Build a trie**

```java
class Trie {

    class TrieNode {
        // Node hiện tại có phải là kết thúc của 1 từ hay không.
        public boolean finished;
        //Lưu map giá trị các cạnh nối sang các con.
        public Map<Character, TrieNode> children;

        public TrieNode() {
            children = new HashMap<>();
        }
    }

    // node gốc
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    /**
     * Thêm 1 từ mới vào từ điển. 
     */
    public void insert(String word) {
        // Bắt đàu từ node gốc
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            TrieNode child = node.children.get(ch);
            //Thêm con mới cho node hiện tại nếu chưa có
            if (child == null) {
                child = new TrieNode();
                node.children.put(ch, child);
            }
            //rồi lại nhảy xuống để xét kí tự tiếp theo của word.
            node = child;
        }
        // đến đây thì node là nút "lá", set giá trị finished cho nó.
        node.finished = true;
    }

    /**
     * Tìm kiếm xem 1 từ có trong từ điển hay không. 
     */
    public boolean search(String word) {
        // bắt đàu từ node gốc 
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            // return false nếu kí tự hiện tại chưa có trong các con của node 
            TrieNode child = node.children.get(ch);
            if (child == null) {
                return false;
            }
            node = child;
        }
        // đến đây thì word có trong trie, nhưng word có trong từ điển hay không phụ thuộc vào node.finished = true hay không.
        // vì nếu node.finished = false thì chứng tỏ word này chỉ là prefix của 1 từ nào đó trong từ điển mà thôi. 
        return node.finished;
    }

    /**
     * Tìm kiếm xem trong từ điển có từ nào prefix là word hay không. 
     */
    public boolean startsWith(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            TrieNode child = node.children.get(ch);
            if (child == null) {
                return false;
            }
            node = child;
        }
        return true;
    }
}


```

Complexity:

- Time:
    - insert: `O(K)` where `K` is length of the word.
    - search: `O(K)` where `K` is length of the word.
    - startsWith: `O(K)` where `K` is length of the word.
- Space: `O(N * K)` where `N` is the number of words in dictionary.

## 6. Maximum XOR of two numbers in an array.

Problem link: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

```java
/**
 * Solution: Build 1 Radix search tree, fix độ cao của trie là 32 tương đương với các số 32 bit.
 */
class Solution {
    class RSTNode {
        public int value;
        RSTNode[] children;

        public RSTNode() {
            children = new RSTNode[2];
        }
    }

    public int findMaximumXOR(int[] nums) {
        RSTNode root = new RSTNode();
        for (int value : nums) {
            insert(root, value);
        }
        int result = 0;
        for (int value : nums) {
            result = Math.max(result, value ^ getXor(root, value));
        }
        return result;
    }

    public void insert(RSTNode root, int value) {
        RSTNode node = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (value >> i) & 1;
            RSTNode child = node.children[bit];
            if (child == null) {
                child = new RSTNode();
                node.children[bit] = child;
            }
            node = child;
        }
        node.value = value;
    }

    public int getXor(RSTNode root, int value) {
        RSTNode node = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (value >> i) & 1;
            // cố gắng đi sang nhánh đối diện để có giá trị XOR lớn nhất
            RSTNode child = node.children[1 - bit];
            if (child == null) {
                child = node.children[bit];
            }
            node = child;
        }
        return node.value;
    }
}
```

- Time: `O(N * K)`, where `N` is length of `array`, `K` is the height of the Radix search tree.
- Space: `O(N * K)`
