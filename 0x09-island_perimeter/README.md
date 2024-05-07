# Island Perimeter
[]() 0x09 []()
---

# Concepts Needed:
## 2D Arrays (Matrices):
* Accessing and iterating over elements in a 2D array.
* Understanding how to navigate through adjacent cells (horizontally and vertically).

## Conditional Logic:
* Applying conditions to determine whether a cell contributes to the perimeter of the island.

## Counting Techniques:
* Developing a method to count the edges that contribute to the island’s perimeter.

## Problem-Solving Strategies:
* Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

## Python Programming:
* Nested loops for iterating over grid cells.
Conditional statements to check the status of adjacent cells.

---

# NEED TO KNOW?
## Python Official Documentation:
* [Nested Lists:](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions) Understanding how to work with lists within lists in Python.

## GeeksforGeeks Articles:
* [Python Multi-dimensional Arrays:](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/) A guide to working with 2D arrays in Python effectively.

## TutorialsPoint:
* [Python Lists:](https://www.tutorialspoint.com/python/python_lists.htm) Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.

## YouTube Tutorials:
* [Python 2D arrays and lists](https://www.youtube.com/watch?v=aNzepGawwCI)

---
```
By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.
```

# Additional Resources
* [Mock Technical Interviews](https://www.youtube.com/watch?v=fFgEM6CMQc4)

---

[`^`](#need-to-know)

---
# Task
## 0-Island Perimeter

Create a function `def island_perimeter(grid)`: that returns the perimeter of the island described in `grid`:

* grid is a list of list of integers:
    * `0` represents `water`
    * `1` represents `land`
    * `Each cell` is `square`, with a side `length of 1`
    * `Cells` are connected `horizontally/vertically` (not diagonally).
    * `grid` is `rectangular`, with its `width` and `height` `not exceeding 100`
* The grid is completely surrounded by water
* There is only one island (or nothing).
* The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
---

[`^`](#need-to-know)

---