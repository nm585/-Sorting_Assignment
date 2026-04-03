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

- **Insertion Sort** is the slowest algorithm and its running time increases rapidly, consistent with its \(O(n^2)\) complexity.
- **Selection Sort** also shows quadratic behavior and performs slightly better than Insertion Sort in this experiment.
- **Merge Sort** performs efficiently and follows \(O(n \log n)\) behavior, making it the fastest algorithm among the three.


---

### Result 2 – Nearly Sorted Arrays (5% noise)
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/34431899-897f-4c64-a543-001117ca5929" />

This experiment measures the running time of the algorithms on nearly sorted arrays.

- **Insertion Sort** improves significantly compared to the random case, because it performs better when the input is close to sorted.
- **Selection Sort** does not improve much, since its running time is still based on repeatedly scanning the unsorted part of the array.
- **Merge Sort** remains stable and efficient, and is still the fastest algorithm in this experiment.


---

### Explanation of Change

- **Insertion Sort** improves because the array is almost sorted, so fewer element shifts are required.
- **Selection Sort** changes much less, because it still performs the same repeated minimum searches regardless of the initial order.
- **Merge Sort** is less affected by input order, so its performance remains relatively stable.

---

## Conclusion

- For random arrays, **Merge Sort** performs best.
- For nearly sorted arrays, **Insertion Sort** improves significantly.
- **Selection Sort** remains relatively slow in both experiments.
- Choosing the right algorithm depends on the structure of the input data.

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
