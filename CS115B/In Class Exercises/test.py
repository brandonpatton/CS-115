def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = low + (high - low) // 2
        print(mid)
        print(high)
        print(low)
        if key < lst[mid]:
            high = mid - 1
        elif key > lst[mid]:
            low = mid + 1
        else:
            return mid
    return -low - 1

print(binary_search(['G', 'F', 'E', 'D', 'C', 'B', 'A'], 'C'))
