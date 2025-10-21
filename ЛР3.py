from logging import *
from random import *
a = []
b = []
c = []
d = []
e = []
f = []

def masiv(n):
    for i in range(1000):
        n.append(randint(1, 101))
    return n
basicConfig(level=INFO, filename='py_log.log', filemode='w', format="%(asctime)s %(levelname)s %(message)s")


print("Пузырьковая сортировка")
print(masiv(a))
def bubble_sort(nums):
    info("The bubble_sort start")
    flag = True
    count = 0
    while flag == True:
        flag = False
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count += 1
                flag = True
    info("The bubble_sort finish ")
    info(f"Number of iterations = {count}")
bubble_sort(a)
print(a)
print()


print("Сортировка выборкой")
print(masiv(b))
def selections_sort(nums):
    info("The selections_sort start")
    count2 = 0
    for i in range(len(nums)):
        lower_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lower_index]:
                lower_index = j
                count2 += 1
        nums[i], nums[lower_index] = nums[lower_index], nums[i]
    info("The selections_sort finish")
    info(f"Number of iterations = {count2}")
selections_sort(b)
print(b)
print()


print("Сортировка вставками")
print(masiv(c))
def insertion_sort(nums):
    info("The insertion_sort start")
    for i in range(1, len(nums)):
        item = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item:
            j -= 1
            nums[j + 1] = item
    info("The insertion_sort finish")
insertion_sort(c)
print(c)
print()


print("Пирамидальная сортировка")
print(masiv(d))

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


info("The heap_sort start")
def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    info("The heap_sort finish")

heap_sort(d)
print(d)
print()


print("Сортировка слиянием")
print(masiv(e))

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


info("The merge_sort start")
def merge_sort(nums):

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)
info("The merge_sort finish")

e = merge_sort(e)
print(e)
print()


print("Быстрая сортировка")
print(masiv(f))

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


info("The quick_sort start")
def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    info("The quick_sort finish")

quick_sort(f)
print(f)
