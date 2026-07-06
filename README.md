# NumPy Learning Log

Documenting my journey learning NumPy for data analysis / ML.

## Progress
- [x] Array creation & basics
- [x] Vectorized operations (arrays vs lists)
- [x] Multidimensional arrays & indexing (chain vs direct)
- [x] Slicing
- [ ] Broadcasting
- [ ] Array operations
- [ ] Practice problems

## What I've learned so far

### Arrays vs Lists
- `list * 2` duplicates the list; `array * 2` multiplies each element (vectorized operation)
- NumPy arrays support element-wise math directly, lists don't

### Multidimensional Indexing
- Chain indexing (`array[0][0][1]`) works but creates intermediate array objects at each step
- Direct multidimensional indexing (`array[1,0,1]`) is faster — single lookup instead of nested ones

### Slicing
- Syntax: `array[start:end:step]` per dimension
- For 2D arrays: `array[row_start:row_end, col_start:col_end]`

## Resources
- (add whatever tutorial/course you're following)

## Notes
Will keep updating this as I go — code and notes organized by topic in folders.
