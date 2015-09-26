__author__ = 'strelkov'


def task(seq):
    """
    Функция принимает последовательность, каждый элемент которой
    может быть другой последовательностью.

    Вернуть плоский отсортированный список всех элементов, в т.ч. и вложенных.

    Пример:
    >>> task([1, 2, 3, (4, 5), [6, 7], {8, 9}])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    # BEGIN
    result_list = []
    for val in seq:
        if isinstance(val, (list, tuple, set)):
            result_list.extend(list(val))
        elif isinstance(val, (int, float)):
            result_list.append(val)
        else:
            return False
    result_list = sorted(result_list)
    return result_list
    # END


def _test_task(seq, expected):
    assert task(seq) == expected


def test_ok():
    _test_task([1, 2, 3, (4, 5), [6, 7], {8, 9}], [1, 2, 3, 4, 5, 6, 7, 8, 9])


def test_empty():
    _test_task(set(), [])


def test_mixed():
    _test_task((set(), (1, ), [42], 1, 99, []), [1, 1, 42, 99])

