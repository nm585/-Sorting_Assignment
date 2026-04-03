## Student Name
Nevo Marmelshtein

## Selected Algorithms
- Selection Sort
- Insertion Sort
- Merge Sort

---

## Run Command

```bash
python run_experiments.py -a 2 3 4 -s 100 500 1000 3000 -e 1 -r 20
```

## Arguments Explanation
- `-a` → Algorithms (2 = Selection, 3 = Insertion, 4 = Merge)
- `-s` → Array sizes
- `-e` → Experiment type (1 = nearly sorted, 5% noise)
- `-r` → Number of repetitions

---

## Results

### Result 1 – Random Arrays
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/6b6d613e-2410-43d0-be34-9623ac7eb7dd" />

This experiment measures the running time of the algorithms on random arrays.

- **Insertion Sort** is the slowest algorithm in this experiment, with running time reaching about **0.18 seconds** for the largest input size. Its average and worst-case time complexity are **O(n²)**.
- **Selection Sort** also shows quadratic growth, reaching about **0.16 seconds** for the largest input size. Its time complexity is **O(n²)**.
- **Merge Sort** performs much more efficiently, with running time staying around **0.006 seconds** even for the largest input. Its time complexity is **O(n log n)**.


---

### Result 2 – Nearly Sorted Arrays (5% noise)
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/34431899-897f-4c64-a543-001117ca5929" />

This experiment measures the running time of the algorithms on nearly sorted arrays.

- **Insertion Sort** improves significantly compared to the random case, with running time reaching only about **0.023 seconds** for the largest input. Its best-case time complexity is **O(n)**, although its worst case is still **O(n²)**.
- **Selection Sort** does not improve much, and its running time still reaches about **0.156 seconds** for the largest input. Its time complexity remains **O(n²)**.
- **Merge Sort** remains stable and efficient, with running time staying around **0.005–0.006 seconds**. Its time complexity is **O(n log n)**.

### Explanation of Change

- **Insertion Sort** improves because the array is almost sorted, so fewer shifts are needed. In such cases, it can get closer to its best-case behavior of **O(n)**.
- **Selection Sort** changes very little, because it still performs the same repeated scans regardless of the initial order.
- **Merge Sort** is less affected by input order, so its running time remains relatively stable.

### Conclusion

- For **random arrays**, **Merge Sort** performs best.
- For **nearly sorted arrays**, **Insertion Sort** improves significantly, but **Merge Sort** still has the lowest running time overall.
- **Selection Sort** remains relatively slow in both experiments.

---

## How to Use

### Example Command (Windows)

```bash
python run_experiments.py -a 2 3 4 -s 100 500 1000 3000 -e 1 -r 20
```

### Example Command (macOS)

```bash
python3 run_experiments.py -a 2 3 4 -s 100 500 1000 3000 -e 1 -r 20
```

### The Interface Allows the User to Choose

- Which algorithms to compare (`-a`)
- Array sizes (`-s`)
- Experiment type / noise level (`-e`)
  - `1` – Nearly sorted with 5% noise
  - `2` – Nearly sorted with 20% noise
- Number of repetitions (`-r`)

### Algorithm IDs

- `1` – Bubble Sort
- `2` – Selection Sort
- `3` – Insertion Sort
- `4` – Merge Sort
- `5` – Quick Sort
