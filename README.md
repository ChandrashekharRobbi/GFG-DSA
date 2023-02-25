# GFG-DSA with Python

I will be writing theory explaination , implmentation and problems based on each section as mentioned in the GFG DSA with python course

I will be using **Jupyter Notebook** as IDE

> Note:  so the links which you see at start of any notebook may not be able to open in Github 

Topics 

1. [Python OOPS](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Python%20(OOPS).ipynb)
2. [Stack](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Stack.ipynb)
3. [Deque](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Deque.ipynb)
4. [Strings](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Strings.ipynb)
5. [Circular Linked List](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Circular%20Linked%20List.ipynb)
6. [Doubly Circular Linked List](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Doubly%20Linked%20List.ipynb)
7. [Tree](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Binary%20Search%20Tree.ipynb)
8. [Sorting](https://github.com/ChandrashekharRobbi/GFG-DSA/blob/main/Sorting.ipynb)





## Cheat Sheet for Big O Notation



**Common Data Structure Operations**


<table>

<tbody>

<tr>

<th>Data Structure</th>

<th >Time Complexity</th>

<th>Space Complexity</th>

</tr>

<tr>

<th></th>

<th >Average</th>

<th >Worst</th>

<th>Worst</th>

</tr>

<tr>

<th></th>

<th>Access</th>

<th>Search</th>

<th>Insertion</th>

<th>Deletion</th>

<th>Access</th>

<th>Search</th>

<th>Insertion</th>

<th>Deletion</th>

<th></th>

</tr>

<tr>

<td>Array</td>

<td>Θ(1)</td>

<td>Θ(n)</td>

<td>Θ(n)</td>

<td>Θ(n)</td>

<td>O(1)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Stack</td>

<td>Θ(n)</td>

<td>Θ(n)</td>

<td>Θ(1)</td>

<td>Θ(1)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(1)</td>

<td>O(1)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Queue</td>

<td>Θ(n)</td>

<td>Θ(n)</td>

<td>Θ(1)</td>

<td>Θ(1)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(1)</td>

<td>O(1)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Singly-Linked List</td>

<td>Θ(n)</td>

<td>Θ(n)</td>

<td>Θ(1)</td>

<td>Θ(1)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(1)</td>

<td>O(1)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Doubly-Linked List</td>

<td>Θ(n)</td>

<td>Θ(n)</td>

<td>Θ(1)</td>

<td>Θ(1)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(1)</td>

<td>O(1)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Skip List</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n log(n))</td>

</tr>

<tr>

<td>Hash Table</td>

<td>N/A</td>

<td>Θ(1)</td>

<td>Θ(1)</td>

<td>Θ(1)</td>

<td>N/A</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Binary Search Tree</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Cartesian Tree</td>

<td>N/A</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>N/A</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

<tr>

<td>B-Tree</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(n)</td>

</tr>

<tr>

<td>Red-Black Tree</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(n)</td>

</tr>

<tr>

<td>Splay Tree</td>

<td>N/A</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>N/A</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(n)</td>

</tr>

<tr>

<td>AVL Tree</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(log(n))</td>

<td>O(n)</td>

</tr>

<tr>

<td>KD Tree</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>Θ(log(n))</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

</tbody>

</table>

**Array Sorting Algorithms**


<table>

<tbody>

<tr>

<th>Algorithm</th>

<th >Time Complexity</th>

<th>Space Complexity</th>

</tr>

<tr>

<th></th>

<th>Best</th>

<th>Average</th>

<th>Worst</th>

<th>Worst</th>

</tr>

<tr>

<td>Quicksort</td>

<td>Ω(n log(n))</td>

<td>Θ(n log(n))</td>

<td>O(n^2)</td>

<td>O(log(n))</td>

</tr>

<tr>

<td>Mergesort</td>

<td>Ω(n log(n))</td>

<td>Θ(n log(n))</td>

<td>O(n log(n))</td>

<td>O(n)</td>

</tr>

<tr>

<td>Timsort</td>

<td>Ω(n)</td>

<td>Θ(n log(n))</td>

<td>O(n log(n))</td>

<td>O(n)</td>

</tr>

<tr>

<td>Heapsort</td>

<td>Ω(n log(n))</td>

<td>Θ(n log(n))</td>

<td>O(n log(n))</td>

<td>O(1)</td>

</tr>

<tr>

<td>Bubble Sort</td>

<td>Ω(n)</td>

<td>Θ(n^2)</td>

<td>O(n^2)</td>

<td>O(1)</td>

</tr>

<tr>

<td>Insertion Sort</td>

<td>Ω(n)</td>

<td>Θ(n^2)</td>

<td>O(n^2)</td>

<td>O(1)</td>

</tr>

<tr>

<td>Selection Sort</td>

<td>Ω(n^2)</td>

<td>Θ(n^2)</td>

<td>O(n^2)</td>

<td>O(1)</td>

</tr>

<tr>

<td>Tree Sort</td>

<td>Ω(n log(n))</td>

<td>Θ(n log(n))</td>

<td>O(n^2)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Shell Sort</td>

<td>Ω(n log(n))</td>

<td>Θ(n(log(n))^2)</td>

<td>O(n(log(n))^2)</td>

<td>O(1)</td>

</tr>

<tr>

<td>Bucket Sort</td>

<td>Ω(n+k)</td>

<td>Θ(n+k)</td>

<td>O(n^2)</td>

<td>O(n)</td>

</tr>

<tr>

<td>Radix Sort</td>

<td>Ω(nk)</td>

<td>Θ(nk)</td>

<td>O(nk)</td>

<td>O(n+k)</td>

</tr>

<tr>

<td>Counting Sort</td>

<td>Ω(n+k)</td>

<td>Θ(n+k)</td>

<td>O(n+k)</td>

<td>O(k)</td>

</tr>

<tr>

<td>CubeSort</td>

<td>Ω(n)</td>

<td>Θ(n log(n))</td>

<td>O(n log(n))</td>

<td>O(n)</td>

</tr>

</tbody>

</table>





Source : [Big O CheatSheet](https://www.bigocheatsheet.com)
