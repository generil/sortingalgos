import math


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value


def hashing(A):
    m = A[0]
    for i in range(1, len(A)):
        if m < A[i]:
            m = A[i]

    result = [m, int(math.sqrt(len(A)))]
    return result


def rehashing(i, code):
    return int(i / code[0] * (code[1] - 1))


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)

        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark += 1

        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            tmp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = tmp

    tmp = alist[first]
    alist[left_mark] = alist[right_mark]
    alist[right_mark] = tmp

    return right_mark

####################################################


def selection_sort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location
        tmp = alist[fillslot]
        alist[fillslot] = alist[position_of_max]
        alist[position_of_max] = tmp


def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                tmp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = tmp


def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = current_value


def shell_sort(alist):
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)

        print("After increments of size {}, The list is {}".format(
            sublist_count, alist))


def bucket_sort(alist):
    code = hashing(alist)
    buckets = [list() for _ in range(code[1])]

    for i in alist:
        x = rehashing(i, code)
        bucket = buckets[x]
        bucket.append(i)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for b in range(len(buckets)):
        for v in buckets[b]:
            alist[index] = v
            index += 1


def radix_sort(alist):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(RADIX)]

        for i in alist:
            tmp = i / placement
            buckets[tmp % RADIX].append(i)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(RADIX):
            bucket = buckets[b]
            for i in bucket:
                alist[a] = i
                a += 1

        placement *= RADIX


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[i]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)
