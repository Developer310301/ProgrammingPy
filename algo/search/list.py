import math


class ListSearching:

    @staticmethod
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    @staticmethod
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    @staticmethod
    def binary_search_recursive(arr, target):
        return ListSearching._binary_search_recursive(arr, target, 0, len(arr) - 1)

    @staticmethod
    def _binary_search_recursive(arr, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return ListSearching._binary_search_recursive(arr, target, mid + 1, high)
        else:
            return ListSearching._binary_search_recursive(arr, target, low, mid - 1)

    @staticmethod
    def interpolation_search(arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high and target >= arr[low] and target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    return low
                return -1

            pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))

            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        return -1

    @staticmethod
    def jump_search(arr, target):
        step = int(math.sqrt(len(arr)))
        prev = 0
        while arr[min(step, len(arr)) - 1] < target:
            prev = step
            step += int(math.sqrt(len(arr)))
            if prev >= len(arr):
                return -1

        while arr[prev] < target:
            prev += 1
            if prev == min(step, len(arr)):
                return -1

        if arr[prev] == target:
            return prev
        return -1