## Student Name
Nevo Marmelshtein

## Selected Algorithms
- Insertion Sort
- Merge Sort
- Quick Sort

---

## Run comend

python3 run_experiments.py -a 3 4 5 -s 100 500 1000 3000 -e 1 -r 20

## Arguments Explanation
- -a  Algorithms (3 = Insertion, 4 = Merge, 5 = Quick)
- -s  Array sizes
- -e  Experiment type (1 = nearly sorted, 5% noise)
- -r  Number of repetitions

---

## Results

### Result 1 – Random Arrays

This experiment measures the running time of the algorithms on random arrays.

- **Insertion Sort** is the slowest algorithm and its running time increases rapidly, consistent with its O(n²) complexity.
- **Merge Sort** performs efficiently and follows O(n log n) behavior.
- **Quick Sort** is the fastest in practice among the tested algorithms.
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/550e6fd7-d003-4755-a036-2a9c11246b98" />

---

### Result 2 – Nearly Sorted Arrays (5% noise)

This experiment measures performance when the arrays are nearly sorted.

- **Insertion Sort** improves significantly compared to the random case.
- **Merge Sort** remains stable and efficient.
- **Quick Sort** is still the fastest algorithm.
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/1aac49f7-b4ff-4408-99c5-72f721590fca" />

---

### Explanation of Change

- **Insertion Sort** improves because the array is almost sorted, so only a few elements need to be moved.
- **Merge Sort** and **Quick Sort** are less affected by the initial order of the array, so their performance remains relatively stable.

---

## Conclusion

- For random arrays Quick Sort and Merge Sort perform best  
- For nearly sorted arrays Insertion Sort improves significantly  
- Choosing the right algorithm depends on the structure of the input data
