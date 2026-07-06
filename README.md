# NumPy Core Concepts & Practices

A comprehensive reference guide and cheat sheet covering fundamental NumPy operations, from basic vectorisation to advanced filtering and broadcasting.

## 📌 Table of Contents
1. [Vectorised Calculation & Indexing](#1-vectorised-calculation--indexing)
2. [Slicing Arrays](#2-slicing-arrays)
3. [Arithmetic Operations](#3-arithmetic-operations)
4. [Comparison & Masking](#4-comparison--masking)
5. [Broadcasting Rules & Applications](#5-broadcasting-rules--applications)
6. [Aggregate Functions](#6-aggregate-functions)
7. [Filtering & Conditional Selection](#7-filtering--conditional-selection)
8. [Random Number Generation (RNG)](#8-random-number-generation-rng)

---

## 1. Vectorised Calculation & Indexing

NumPy processes operations element-wise (vectorisation) without using explicit `for` loops, unlike native Python lists.

```python
import numpy as np

my_list = [1, 2, 3, 4]
print(my_list * 2)      # Output: [1, 2, 3, 4, 1, 2, 3, 4] (Duplicates list)

array = np.array(my_list)
print(array * 2)        # Output: [2, 4, 6, 8] (Multiplies element-wise)
```

### Multidimensional Array Indexing
Multidimensional indexing (`array[x, y, z]`) is significantly **faster** and more memory-efficient than chain indexing (`array[x][y][z]`).

```python
array_3d = np.array([[[1, 2, 3], ,  [7, 8, 9]],
                     [[10,11,13],[13,14,15],[16,17,18]],
                     [[19,20,21],[21,22,23],[24,25,26]]])

# Chain Indexing
print(array_3d[0][0][1])  # Output: 2

# Multidimensional Indexing (Faster)
print(array_3d[1, 0, 1])  # Output: 11
```

---

## 2. Slicing Arrays
Slicing follows the standard syntax: `array[start:end:step]` across any specific dimension axis.

```python
array = np.array([[1,  2,  3,  4],
,
 ,
                  [13, 14, 15, 16]])

# Extract rows 0 to 2 and columns 0 to 1
print(array[0:3, 0:2])
# Output:
# [[1, 2],
#,
#]
```

---

## 3. Arithmetic Operations

### Scalar Arithmetic
```python
array = np.array([1, 2, 3])
print(array + 1)   # [2, 3, 4]
print(array ** 5)  # [1, 32, 243]
```

### Element-Wise Arithmetic (Two Arrays)
```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)  # [5, 7, 9]
print(array1 * array2)  # [4, 10, 18]
```

### Vectorised Math Functions
```python
temp = np.sqrt(array)
print(np.round(temp))  # Rounds element-wise
print(np.pi)           # Constant pi
```

---

## 4. Comparison & Masking
Boolean evaluations create binary masks that allow for rapid analysis or value mutation.

```python
scores = np.array([91, 55, 100, 64, 78, 82])

print(scores == 100)  # [False, False,  True, False, False, False]
print(scores >= 60)   # [ True, False,  True,  True,  True,  True]

# Masking Mutation: Set all failing scores (< 60) to 0
scores[scores < 60] = 0
print(scores)         # [91, 0, 100, 64, 78, 82]
```

---

## 5. Broadcasting Rules & Applications
Broadcasting allows NumPy to perform operations on arrays with differing shapes by virtually stretching dimensions.

### 📐 Broadcasting Criteria
Two dimensions are compatible if:
1. They have the exact same size.
2. One of the dimensions has a size of **1**.

### Practical Exercise: Creating a Multiplication Table (1 to 10)
```python
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])           # Shape: (1, 10)
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) # Shape: (10, 1)

# Multiplies (10, 1) by (1, 10) to create a matching (10, 10) grid
print(array2 * array1)
```

---

## 6. Aggregate Functions
Aggregates compress array structures into descriptive summaries or check for directional index trends along targeted axes.

```python
array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(np.sum(array))         # 55
print(np.mean(array))        # 5.5
print(np.argmax(array))      # 9 (Index of flat array maximum)

# Axis-specific computations
print(np.sum(array, axis=0)) # Column sums -> [7, 9, 11, 13, 15]
print(np.sum(array, axis=1)) # Row sums    -> [15, 40]
```

---

## 7. Filtering & Conditional Selection

### Logical Filtering
Extract elements matching complex conditions using bitwise operators (`&`, `|`).

```python
ages = np.array([[11, 16, 18, 19, 21, 65], 
                 [21, 19, 98, 94, 95, 24]])

teenagers = ages[ages < 18]               # [11, 16]
adults = ages[(ages >= 18) & (ages < 65)] # [18, 19, 21, 21, 19, 24]
```

### Conditional Vector Assignment (`np.where`)
`np.where(condition, value_if_true, value_if_false)` modifies or masks datasets cleanly.

```python
# Keep age if >= 18, otherwise replace with 0
adults_only = np.where(ages >= 18, ages, 0)
```

---

## 8. Random Number Generation (RNG)
Modern NumPy practices use `default_rng()` for optimized random workflows.

```python
# Initialize the recommended Generator instance with a fixed seed
rng = np.random.default_rng(seed=1)

# Generate integers between 1 and 100
print(rng.integers(low=1, high=101, size=(3, 2)))

# Shuffle an array in-place
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)



# Sample a random matrix from an array with replacement
print(rng.choice(array, size=(3, 3)))

# Uniform distribution float generation
print(np.random.uniform(low=-1, high=1, size=(3, 2)))
```


## Resources
- https://youtu.be/VXU4LSAQDSc?si=GVzclaUuO-WhID_e
