import argparse
import random
import time
import matplotlib.pyplot as plt
import statistics


# This program compares selected sorting algorithms
# on random arrays and nearly sorted arrays.


def main():
    # Read command line arguments from the user
    args = parse_arguments()

    # Map each algorithm ID to its name and function
    algorithm_map = {
        1: ("Bubble Sort", bubble_sort),
        2: ("Selection Sort", selection_sort),
        3: ("Insertion Sort", insertion_sort),
        4: ("Merge Sort", merge_sort),
        5: ("Quick Sort", quick_sort)
    }

    # Build a list of the algorithms chosen by the user
    selected_algorithms = [algorithm_map[alg_id] for alg_id in args.a]

    # Get array sizes and number of repetitions from the arguments
    sizes = args.s
    runs = args.r

    # Choose noise level for nearly sorted arrays
    if args.e == 1:
        noise = 0.05
    else:
        noise = 0.20

    # Define the two experiments:
    # 1. Random arrays
    # 2. Nearly sorted arrays with the selected noise level
    test_cases = [
        ("result1.png", create_random_array, "Runtime Comparison (Random Arrays)"),
        (
            "result2.png",
            lambda size: create_nearly_sorted_array(size, noise),
            f"Runtime Comparison (Nearly Sorted, noise={int(noise * 100)}%)"
        )
    ]

    # Run both experiments
    for file_name, array_generator, graph_title in test_cases:
        # Dictionary for storing average and standard deviation for each algorithm
        results = {}

        # Initialize the results dictionary dynamically according to selected algorithms
        for algorithm_name, _ in selected_algorithms:
            results[algorithm_name] = {"avg": [], "std": []}

        # Run the experiment for each array size
        for size in sizes:
            # Store all measured times for each algorithm for the current size
            times_by_algorithm = {}

            # Initialize an empty list of times for each algorithm
            for algorithm_name, _ in selected_algorithms:
                times_by_algorithm[algorithm_name] = []

            # Repeat the experiment several times for reliability
            for i in range(runs):
                # Generate an array of the current size
                arr = array_generator(size)

                # Measure the running time of each selected algorithm
                for algorithm_name, algorithm_function in selected_algorithms:
                    elapsed_time = measure_time(algorithm_function, arr)
                    times_by_algorithm[algorithm_name].append(elapsed_time)

            # After all repetitions, compute average and standard deviation
            for algorithm_name, _ in selected_algorithms:
                results[algorithm_name]["avg"].append(
                    statistics.mean(times_by_algorithm[algorithm_name])
                )
                results[algorithm_name]["std"].append(
                    statistics.stdev(times_by_algorithm[algorithm_name])
                )

        # Start drawing the graph
        plt.figure()

        # Draw a curve for each selected algorithm
        for algorithm_name, _ in selected_algorithms:
            averages = results[algorithm_name]["avg"]
            deviations = results[algorithm_name]["std"]

            # Plot average runtime with error bars
            plt.errorbar(sizes, averages, yerr=deviations, label=algorithm_name, marker='o')

            # Fill the area between avg-std and avg+std
            plt.fill_between(
                sizes,
                [avg - std for avg, std in zip(averages, deviations)],
                [avg + std for avg, std in zip(averages, deviations)],
                alpha=0.2
            )

        # Add labels, title, legend, and grid
        plt.xlabel("Array size (n)")
        plt.ylabel("Running Time (seconds)")
        plt.title(graph_title)
        plt.legend()
        plt.grid(True)

        # Save the graph and show it
        plt.savefig(file_name)
        plt.show()


def parse_arguments():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Run sorting experiments")

    # Algorithms to compare
    parser.add_argument(
        "-a",
        nargs="+",
        type=int,
        required=True,
        help="Algorithm IDs: 1-Bubble, 2-Selection, 3-Insertion, 4-Merge, 5-Quick"
    )

    # Array sizes to test
    parser.add_argument(
        "-s",
        nargs="+",
        type=int,
        required=True,
        help="Array sizes, for example: 100 500 3000"
    )

    # Experiment type / noise level
    parser.add_argument(
        "-e",
        type=int,
        required=True,
        choices=[1, 2],
        help="Experiment type: 1-nearly sorted 5%% noise, 2-nearly sorted 20%% noise"
    )

    # Number of repetitions
    parser.add_argument(
        "-r",
        type=int,
        required=True,
        help="Number of repetitions"
    )

    # Return parsed arguments
    return parser.parse_args()


def create_random_array(size):
    # Create an array of random integers
    return [random.randint(0, 100000) for _ in range(size)]


def create_nearly_sorted_array(size, noise=0.05):
    # Start with a sorted array
    arr = list(range(size))

    # Number of random swaps according to noise level
    num_swaps = int(size * noise)

    # Perform random swaps to add noise
    for _ in range(num_swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def measure_time(sort_function, arr):
    # Copy the array so the original input is not changed
    copied_arr = arr[:]

    # Measure running time
    start = time.perf_counter()
    sort_function(copied_arr)
    end = time.perf_counter()

    return end - start


def bubble_sort(arr):
    # Bubble Sort implementation
    result = arr[:]
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # Stop early if no swaps were made
        if not swapped:
            break

    return result


def selection_sort(arr):
    # Selection Sort implementation
    result = arr[:]
    n = len(result)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]

    return result


def insertion_sort(arr):
    # Insertion Sort implementation
    result = arr[:]

    for i in range(1, len(result)):
        current_value = result[i]
        j = i - 1

        while j >= 0 and result[j] > current_value:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current_value

    return result


def merge_sort(arr):
    # Merge Sort implementation
    if len(arr) <= 1:
        return arr[:]

    middle = len(arr) // 2
    left_part = merge_sort(arr[:middle])
    right_part = merge_sort(arr[middle:])

    return merge(left_part, right_part)


def merge(left, right):
    # Merge step of Merge Sort
    merged = []
    i = 0
    j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from left
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add remaining elements from right
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def quick_sort(arr):
    # Quick Sort implementation
    if len(arr) <= 1:
        return arr[:]

    # Choose the middle element as pivot
    pivot = arr[len(arr) // 2]

    smaller = []
    equal = []
    greater = []

    # Split elements relative to the pivot
    for value in arr:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            greater.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(greater)


if __name__ == "__main__":
    main()