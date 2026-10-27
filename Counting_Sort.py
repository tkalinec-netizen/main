
import numpy as np
def main():
    examples = [
        [4, 2, 2, 8, 3, 3, 1],
        [2, -1, 0, -3, -5],
        [],
    ]

    for array in examples:
        print("Input:", array)
        print("Counting sort:", SortAlgorithm.CountingSort(array))
        print("Bubble sort:", SortAlgorithm.BubbleSort(array))


class SortAlgorithm:
    @staticmethod
    def CountingSort(array)-> list:
        if not array:
            return []

        minimum = min(array)
        maximum = max(array)
        counts =  np.zeros(maximum-minimum+1, dtype=int) #[0] * (maximum - minimum + 1)

        for value in array:
            counts[value - minimum] += 1

        sorted_array = []
        for offset, count in enumerate(counts):
            sorted_array.extend([offset + minimum] * count)

        return sorted_array

    @staticmethod
    def BubbleSort(array):

        sorted_array = array.copy() 
        for i in range(len(sorted_array)): 
            for j in range(0, len(sorted_array) - i - 1):
                if sorted_array[j] > sorted_array[j + 1]:
                    sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

        return sorted_array


if __name__ == "__main__":
    main()


import pytest


@pytest.mark.parametrize(
    ("array", "expected"),
    [
        ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8]),
        ([2, -1, 0, -3, -5], [-5, -3, -1, 0, 2]),
        ([], []),
    ],
)
def test_counting_sort(array, expected, request):
    result = SortAlgorithm.CountingSort(array)
    print(f"Input: {array} -> Output: {result}")
    successful = result == expected
    test_number = request.node.callspec.indices["array"] + 1
    with open(f"test_{test_number:02d}.txt", "w", encoding="utf-8") as output_file:
        output_file.write(f"Input: {array}\nOutput: {result}\nSuccessful: {successful}\n")
    assert successful

    