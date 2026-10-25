def main():
    examples = [
        [4, 2, 2, 8, 3, 3, 1],
        [-5, -1, -3, 0, 2],
        [],
    ]

    for array in examples:
        print("Input:", array)
        print("Output:", SortAlgorithm.CountingSort(array))


class SortAlgorithm:
    @staticmethod
    def CountingSort(array):
        if not array:
            return []

        minimum = min(array)
        maximum = max(array)
        counts = [0] * (maximum - minimum + 1)

        for value in array:
            counts[value - minimum] += 1

        sorted_array = []
        for offset, count in enumerate(counts):
            sorted_array.extend([offset + minimum] * count)

        return sorted_array


if __name__ == "__main__":
    main()


import pytest


@pytest.mark.parametrize(
    ("array", "expected"),
    [
        ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8]),
        ([-5, -1, -3, 0, 2], [-5, -3, -1, 0, 2]),
        ([], []),
    ],
)
def test_counting_sort(array, expected):
    result = SortAlgorithm.CountingSort(array)
    print(f"Input: {array} -> Output: {result}")
    assert result == expected

    