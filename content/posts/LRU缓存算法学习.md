+++
title = "LRU 缓存算法学习"
date = 2026-03-12T10:30:00+08:00
draft = false
description = "LRU 与带 TTL 的 LRU 实现笔记，基于 HashMap + 双向链表，附关键注释与复杂度说明。"
tags = ["算法", "缓存", "Java", "LRU"]
+++

这篇记录我学习的两个实现：

1. 标准 LRU（固定容量）  
2. 带 TTL 的 LRU（容量淘汰 + 过期淘汰）

核心思路都是 `HashMap + 双向链表`：  
`HashMap` 负责 O(1) 定位节点，链表负责 O(1) 维护最近使用顺序。

## 普通 LRU 缓存

```java
import java.util.HashMap;
import java.util.Map;

class LRUCache {

    // 双向链表节点：保存 key/value，便于 O(1) 删除和移动
    private static class Node {
        int key, value;
        Node prev, next;

        Node(int k, int v) {
            key = k;
            value = v;
        }
    }

    private final int capacity;
    // 哨兵节点（循环链表），减少头尾判空逻辑
    private final Node dummy = new Node(0, 0);
    private final Map<Integer, Node> keyToNode = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        dummy.prev = dummy;
        dummy.next = dummy;
    }

    // 查询：命中后需要提升为“最近使用”
    public int get(int key) {
        Node node = getNode(key);
        return node != null ? node.value : -1;
    }

    // 写入：
    // 1) 已存在：更新值并提升到头部
    // 2) 不存在：新建节点插头部，超容量则淘汰尾部（最久未使用）
    public void put(int key, int value) {
        Node node = getNode(key);
        if (node != null) {
            node.value = value;
            return;
        }

        node = new Node(key, value);
        keyToNode.put(key, node);
        pushFront(node);

        if (keyToNode.size() > capacity) {
            Node backNode = dummy.prev;
            keyToNode.remove(backNode.key);
            remove(backNode);
        }
    }

    // 命中节点后移到链表头部，表示最近使用
    private Node getNode(int key) {
        if (!keyToNode.containsKey(key)) {
            return null;
        }
        Node node = keyToNode.get(key);
        remove(node);
        pushFront(node);
        return node;
    }

    // O(1) 从链表移除节点
    private void remove(Node x) {
        x.prev.next = x.next;
        x.next.prev = x.prev;
    }

    // O(1) 插入到头部（dummy 后面）
    private void pushFront(Node x) {
        x.prev = dummy;
        x.next = dummy.next;
        x.prev.next = x;
        x.next.prev = x;
    }
}
```

## TTL LRU 缓存

```java
import java.util.HashMap;
import java.util.Map;

class LRUCache {

    // 在普通节点上增加 expireAt（过期时间戳）
    private static class Node {
        int key, value;
        long expireAt;
        Node prev, next;

        Node(int k, int v, long expireAt) {
            key = k;
            value = v;
            this.expireAt = expireAt;
        }
    }

    private final int capacity;
    private final long ttlMillis;
    private final Node dummy = new Node(0, 0, 0);
    private final Map<Integer, Node> keyToNode = new HashMap<>();

    public LRUCache(int capacity, long ttlMillis) {
        this.capacity = capacity;
        this.ttlMillis = ttlMillis;
        dummy.prev = dummy;
        dummy.next = dummy;
    }

    public int get(int key) {
        Node node = getNode(key);
        return node != null ? node.value : -1;
    }

    public void put(int key, int value) {
        Node node = keyToNode.get(key);
        long expireAt = System.currentTimeMillis() + ttlMillis;

        if (node != null) {
            // 已存在但过期：先删旧节点，再按新节点写入
            if (isExpired(node)) {
                remove(node);
                keyToNode.remove(key);
            } else {
                // 已存在且未过期：更新值 + 刷新过期时间 + 提升到头部
                node.value = value;
                node.expireAt = expireAt;
                remove(node);
                pushFront(node);
                return;
            }
        }

        node = new Node(key, value, expireAt);
        keyToNode.put(key, node);
        pushFront(node);

        // 先清理尾部连续过期节点，再做容量淘汰
        evictExpiredFromTail();

        if (keyToNode.size() > capacity) {
            Node backNode = dummy.prev;
            keyToNode.remove(backNode.key);
            remove(backNode);
        }
    }

    private Node getNode(int key) {
        Node node = keyToNode.get(key);
        if (node == null) {
            return null;
        }

        // 读到过期节点：直接删除并返回 miss
        if (isExpired(node)) {
            remove(node);
            keyToNode.remove(key);
            return null;
        }

        remove(node);
        pushFront(node);
        return node;
    }

    private boolean isExpired(Node node) {
        return System.currentTimeMillis() > node.expireAt;
    }

    // 从尾部批量清理过期节点，降低无效占用
    private void evictExpiredFromTail() {
        while (dummy.prev != dummy && isExpired(dummy.prev)) {
            Node node = dummy.prev;
            remove(node);
            keyToNode.remove(node.key);
        }
    }

    private void remove(Node x) {
        x.prev.next = x.next;
        x.next.prev = x.prev;
    }

    private void pushFront(Node x) {
        x.prev = dummy;
        x.next = dummy.next;
        dummy.next.prev = x;
        dummy.next = x;
    }
}
```

## 简短说明

- 时间复杂度：`get/put` 平均 O(1)
- 空间复杂度：O(capacity)
- 带 TTL 的版本是“惰性过期”：访问或写入时触发清理，不是定时全量扫描。

后续可以继续优化：

1. 线程安全版本（`ReentrantLock` 或分段锁）
2. 更精细的过期清理策略（时间轮 / 最小堆）
3. 统计命中率与淘汰原因（容量淘汰 vs 过期淘汰）
