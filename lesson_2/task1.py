__author__ = 'strelkov'
# ######
# task 1
# ######


def task(seq1, seq2):
    """
    Функция принимает две последовательности (списки, словари, множества).
    Вернуть отсортированный список элементов, каждый из которых принадлежит обеим последовательностям.

    Пример:
    >>> task([1, 3, 2], (2, 3, 4))
    [2, 3]
    """
    return sorted(set(seq1) & set(seq2))


# and tests for this function


def _test_task(seq1, seq2, expected):
    assert task(seq1, seq2) == expected


def test_ok():
    _test_task([1, 2, 3], [2, 3, 4], [2, 3])


def test_list_tuple():
    _test_task(['foo', True, 42], (True, 42, 'baz'), [True, 42])


def test_tuple_set():
    _test_task((99, 22, 11, 44), {'test', 99, 22.0}, [22.0, 99])


def test_empty():
    _test_task({1, 2, 3}, {6, 5, 4}, [])
