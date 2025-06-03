import timeit
import random
import heapq

# Сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Створення тестових даних
sizes = [1000, 5000, 10000]
tests = {size: [random.randint(0, 100000) for _ in range(size)] for size in sizes}

# Вимірювання часу
def measure_time(func):
    return timeit.timeit(func, number=1)

results = {}

for size, data in tests.items():
    results[size] = {
        "Сортування злиттям (Merge Sort)": measure_time(lambda: merge_sort(data[:])),
        "Сортування вставками (Insertion Sort)": measure_time(lambda: insertion_sort(data[:])),
        "Вбудований Timsort (sorted)": measure_time(lambda: sorted(data[:])),
        "Вбудований Timsort (sort)": measure_time(lambda: data[:].sort())
    }

# Вивід результатів
print("Час сортування:")
for size, timings in results.items():
    print(f"\nРозмір списку: {size} елементів")
    for method, time_taken in timings.items():
        print(f"{method}: {time_taken:.6f} сек")

# --- Необов'язкове завдання: об'єднання k списків ---

def merge_k_lists(lists):
    return list(heapq.merge(*lists))

# Перевірка
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("\nВідсортований список (merge_k_lists):", merged_list)