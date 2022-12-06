class ListSorting:

    @staticmethod
    def bubble_sort(arr, reverse=False):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if reverse:
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                else:
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def selection_sort(arr, reverse=False):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if reverse:
                    if arr[min_index] < arr[j]:
                        min_index = j
                else:
                    if arr[j] < arr[min_index]:
                        min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr, reverse=False):

        for i in range(1, len(arr)):
            j = i
            
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        return arr

    @staticmethod
    def merge_sort(arr, reverse=False):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = ListSorting.merge_sort(arr[:mid], reverse)
        right = ListSorting.merge_sort(arr[mid:], reverse)

        return ListSorting._merge(left, right, reverse)

    @staticmethod
    def _merge(left, right, reverse=False):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):

            if reverse:
                if left[i] > right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            else:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

        result += left[i:]
        result += right[j:]

        return result

    @staticmethod
    def quick_sort(arr, reverse=False):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        if reverse:
            left = [x for x in arr if x > pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x < pivot]
        else:
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]

        return ListSorting.quick_sort(left) + middle + ListSorting.quick_sort(right)

    @staticmethod
    def heap_sort(arr):
        pass

    @staticmethod
    def radix_sort(arr):
        pass

    @staticmethod
    def bucket_sort(arr):
        pass

    @staticmethod
    def shell_sort(arr):
        pass

    @staticmethod
    def comb_sort(arr):
        pass

    @staticmethod
    def cocktail_sort(arr):
        pass

    @staticmethod
    def gnome_sort(arr):
        pass

    @staticmethod
    def bitonic_sort(arr):
        pass

    @staticmethod
    def pancake_sort(arr):
        pass

    @staticmethod
    def cycle_sort(arr):
        pass

    @staticmethod
    def bogo_sort(arr):
        pass

    @staticmethod
    def stooge_sort(arr):
        pass

    @staticmethod
    def bead_sort(arr):
        pass

    