# Union-find and Topological sorting


## 1. Union-find

Link problem: lecture slide

**Solution 1: without optimization**
```java
class MyGraph {
  int n;
  int[] parent;

  public MyGraph(int n) {
    this.n = n;
    this.parent = new int[n];
    Arrays.fill(parent, -1);
  }
  
  public void add(int i, int j) {
    int u = find(i);
    int v = find(j);
    if (u != v) {
      union(u,v);
    }
  }
  
  public boolean query(int i, int j) {
    return find(i) == find(j);
  }
  
  //Tìm gốc của cây chứa đỉnh i
  public int find(int i) {
    while(parent[i] != -1) {
        i = parent[i];
    }
    return  i;
  }
  // Hợp nhất 2 cây gốc i và j
  public void union(int i, int j) {
    parent[j] = i;
  }
}
```

Complexity:

- Time: 
  - add(i,j):`O(N)` where `N` the number of nodes.
  - query(i,j): `O(N)` where `N` the number of nodes.
- Space: `O(N)`


**Solution 2: with optimization**
```java
class MyGraph {
  int n;
  int[] parent;
  int[] height;
  
  public MyGraph(int n) {
    this.n = n;
    this.parent = new int[n];    
    Arrays.fill(parent, -1);
    this.height = new int[n];
    Arrays.fill(height, 1);
  }
  
  public void add(int i, int j) {
    int u = find(i);
    int v = find(j);
    if (u != v) {
      union(u,v);
    }
  }
  
  public boolean query(int i, int j) {
    return find(i) == find(j);
  }

  public int find(int i) {
    int root = i;
    while(parent[root] != -1) {
      root = parent[root];
    }
    while(i != root) {
      int u = parent[i];
      parent[i] = root;
      i = u;
    }
    return root;
  }
  
  public void union(int i, int j) {
    if (height[i] > height[j]) {
      parent[j] = i;
    } else if (height[i] < height[j]) {
      parent[i] = j;
    } else {
      parent[i] = j;
      height[j]++;
    }
  }
}
```
- Time:
  - add(i,j): approximate `O(1)`
  - query(i,j): approximate `O(1)`
- Space: `O(N)`


## 2.   Most Stones Removed with Same Row or Column

Link problem: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

```java
class Solution {
  public int removeStones(int[][] stones) {
    int n = stones.length;
    int[] parent = new int[n];
    Arrays.fill(parent, - 1);
    for(int i = 0; i < n; i++) {
      for(int j = i + 1; j < n; j++) {
        if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
          int u = find(i, parent);
          int v = find(j, parent);
          if (u != v) {
            union(u,v, parent);
          }
        }
      }
    }
    int result = 0;
    for(int i = 0; i < n; i++) {
      if (parent[i] == -1) {
        result++;
      }
    }
    return n - result;
  }

  public int find(int i, int[] parent) {
    int root = i;
    while(parent[root] != -1) {
      root = parent[root];
    }
    while(i != root) {
      int u = parent[i];
      parent[i] = root;
      i = u;
    }
    return root;

  }

  public void union(int i, int j, int[] parent) {
    parent[i] = j;
  }
}
```

Complexity:
- Time: `O(N*N))` where `N` is the length of stones. 
- Space: `O(N*N)`

## 3.   The Earliest Moment When Everyone Become Friends

Link problem: https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

```java
class Solution {
  public int earliestAcq(int[][] logs, int n) {
    Arrays.sort(logs, (a,b)->{
      return Integer.compare(a[0],b[0]);
    });
    int[] parent = new int[n];
    Arrays.fill(parent, -1);
    int count = n;
    for(int x = 0; x < logs.length; x++) {
      int[] log = logs[x];
      int i = find(log[1], parent), j = find(log[2], parent);
      if (i != j) {
        count--;
        union(i,j, parent);
        if (count == 1) {
          return log[0];
        }
      }
    }
    return -1;
  }

  public int find(int i, int[] parent) {
    while(parent[i] != -1) {
      i = parent[i];
    }
    return i;
  }

  public void union(int i, int j, int[] parent) {
    parent[i] = j;
  }
}

```

Complexity:

- Time: `O(N*LogN)` where `N` is the length of logs.
- Space: `O(N)`

## 4. Topological sorting

Problem link: in lecture slide


```java
class Topo {
  int n;
  int[] degree;
  Map<Integer, Set<Integer>> edgeMap;
  boolean[] visited;

  public Topo(int n, int[][] edges) {
    this.n = n;
    this.degree = new int[n];
    this.visited = new boolean[n];
    Arrays.fill(visited, false);
    this.edgeMap = new HashMap<>();

    for(int i = 0; i < n; i++) {
      edgeMap.put(i, new HashSet<>());
    }
    for(int[] edge: edges) {
      int u = edge[0], v = edge[1];
      edgeMap.get(u).add(v);
      degree[v]++;
    }
  }

  //O(M + N)
  public List<Integer> sortUsingBFS() {
    List<Integer> result = new ArrayList<>();
    Deque<Integer> queue = new LinkedList<>();
    for(int i = 0; i < n; i++) { //O(N)
      if (degree[i] == 0) {
        queue.addLast(i);
      }
    }

    //O(M) voi M la so canh cua do thi
    while(!queue.isEmpty()) {
      int i = queue.removeFirst();
      result.add(i);
      for(int j: edgeMap.get(i)) {
        degree[j]--;
        if (degree[j] == 0) {
          queue.addLast(j);
        }
      }
    }
    return result;
  }

  public List<Integer> sortUsingDFS() {
    List<Integer> result = new ArrayList<>();
    for(int i = 0; i < n; i++) {
      if (!visited[i]) {
        dfs(i, result);
      }
    }
    Collections.reverse(result);
    return result;
  }

  public void dfs(int i, List<Integer> result) {
    visited[i] = true;
    for(int j: edgeMap.get(i)) {
      if (!visited[j]) {
        dfs(j,result);
      }
    }
    result.add(i);
  }
}


```

Complexity:

- Time: `O(M+N)` where `M` is the number of edges, `N` is the number of vertices.  
- Space: `O(N)`
