import timeit
import random


# Сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Сортування вставками (Insertion Sort)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key 
    return lst

# Створення випадкових даних
sizes = [1000, 5000, 10000]
tests = {}
for size in sizes:
    tests[size] = [random.randint(0, 100000) for _ in range(size)]

# Вимірювання часу обробки даних
def measure_time(sort_function, arr):
    return timeit.timeit(lambda: sort_function(arr[:]), number=1)

results = {}
for size, data in tests.items():
    results[size] = {
        "Сортування злиттям (Merge Sort)": measure_time(merge_sort, data),
        "Сортування вставками (Insertion Sort)": measure_time(insertion_sort, data),
        "Вбудований Timsort (sorted)": measure_time(sorted, data),
        "Вбудований Timsort (sort)": measure_time(lambda x: x.sort(), data)
    }

print("Час сортування:")
for size, timing in results.items():
    print(f"\nРозмір списку: {size} елементів")
    for sort_type, time_taken in timing.items():
        print(f"{sort_type}: {time_taken:.6f} sec")