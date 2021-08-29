# BFS /DFS

Depth-First Search  (DFS) is an algorithm that searches deep part of graph first. Graph is expressed with Node(Vertex) and Edge. Searching Graph is starting from one node and visiting other nodes. If two nodes are connected, they are called 'adjacent'.

DFS is using stack and it works in flows under this.

1. Put starting node in the stack and check this node as visited.
2.  Take top node on stack and if there are adjacent nodes which are not visited, put them in the stack. If there is no nodes to put, take another node on the top the stack. 
3.  Repeat 2 until it it impossible to take node from the stack.



Breadth First Search(BFS) searches near part of the starting node first. BFS uses queue instead of stack. Stack uses pop(), but queue needs to use pop(0), if we use list. Since pop(0) is slow, we'd better use `from collections import deque` and deque. 

BFS' Flow

1. Put starting node in the queue and check this node as visited.
2.  Take a node(which lies in bottom) and put adjacent nodes which is not visited in queue and check them visited. 
3.  Repeat 2 until it it impossible to take node from the queue.





# Sorting

Sorting is putting data in the order of specific criteria. Sorting may affect time complexity, so choosing adequete sort is very important. If we sorted data, it is possible to use binary search. Sorting is not only a powerful algorithm to solve a problem but also preprocessing for binary search. There are tones of sorting algorithm, studying all kinds of it takes a lot of time, so we need to keep studying sorting algorithm. Let's start it with 3 basic sorting algorithms.

### 1.Selection Sort

selection sort is taking minimum data and change it with the first one. And taking the minimum except the first and changing it with the second. Repeat this until the end is the Selection Sort.

Time complexity is N + (N-1) + (N-2) .... +1 = ( N^2+ N ) / 2, so O(N^2).

It is very brutal way to sort data, but in coding problem, there are many problems which make us figure out the minimum data, selection sort still works in many parts.

### 2.Insertion Sort 

Insertion sort is starting from the second one and compare to the first one. If the second is bigger, go to the third. Else, change the first and the second. Do this until the end. This is Insertion sort. 

Time complexity is 1+2+3 .... (N-1) + N = ( N^2+ N ) / 2, so O(N^2).

But if the data is almost sorted in the order, which means the best case, it takes O(N). O(N) is faster than quick sort, and there is little overhead except the search. 

### 3. Quick Sort

Quick sort is the most popular algorithm among three. Quick sort uses a pivot. Pivot is a criteria to swap data. Pivot selection is very important part of quick sort because it influences time complexity.

Lomuto Partion:

Pivot is the last one in data.

Quick sort is using left and right pointers which start from the left(0 in the list), left goes until it meets data smaller than pivot, and right goes until it meets data bigger than pivot. When both of them stop, swap two data and left and right pointer go to the next one. When right reaches the end, swap pivot and data pointed by left. Now there are smaller data on the left of pivot and bigger are on the right. Do it on the left data and the right. Repeat until it is over, sorting is completed. 

It takes O(NlogN) on average but in worst case, it take O(N^2), so selecting an adequete pivot is very importan part of it.
