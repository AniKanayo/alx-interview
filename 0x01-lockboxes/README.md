# Unlock All Boxes

## Description

You have a set of locked boxes in front of you, numbered sequentially from 0 to n - 1.
Each box may contain keys to other boxes. Your task is to determine whether it is possible to unlock all the boxes.

The `canUnlockAll` method takes a list of lists (`boxes`) as input, 
where each inner list represents a box and contains the keys to other boxes.
A key with the same number as a box can open that box. The first box (`boxes[0]`) is initially unlocked.

The method returns `True` if all the boxes can be opened, and `False` otherwise.

## Method Signature

```python
def canUnlockAll(boxes: List[List[int]]) -> bool:
    pass
```

## Constraints

- The input list `boxes` is a list of lists, where each inner list represents a box and contains the keys to other boxes.
- All keys will be positive integers.
- There can be keys that do not have corresponding boxes.
- The first box (`boxes[0]`) is unlocked.

## Examples

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
# Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
# Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
# Output: False
```

## Approach

The method uses a breadth-first search (BFS) algorithm to explore the boxes and their corresponding keys.
It starts with the first box (`boxes[0]`) as the initial unlocked box and maintains a set to keep track of the visited boxes.

1. Initialize a set to track visited boxes and add the first box (index 0) to the set.
2. Initialize a queue with the first box.
3. While the queue is not empty:
   - Pop the first box from the queue.
   - Check the keys in the current box.
   - For each key, if it corresponds to a valid box index and the box has not been visited before,
add the key to the visited set and enqueue the key.
   - If the visited set contains all the boxes, return `True`.
4. If all boxes cannot be visited, return `False`.

The method follows this approach to determine if all boxes can be opened based on the given keys in each box.

---

Feel free to modify and enhance the README file based on your requirements and preferences.
