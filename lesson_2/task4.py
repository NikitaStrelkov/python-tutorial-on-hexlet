__author__ = 'strelkov'


def task(seq):
    """
    Функция принимает последовательность (список, кортеж или множество).
    Вернуть словарь вида {V: N}, где V -- элемент последовательности,
    N -- сколько раз элемент встречается в последовательности.

    Пример:
    >>> task([10, 20, 20, 21, 30, 21])
    {10: 1, 20: 2, 21: 2, 30: 1}
    """
    # BEGIN
    res = {}
    seq = list(seq)
    for val in seq:
        if val not in res:
            res[val] = seq.count(val)
    return res
    # END


def _test_task(seq, expected):
    assert task(seq) == expected


def test_ok():
    _test_task([10, 20, 20, 21, 30, 21],
               {10: 1, 20: 2, 21: 2, 30: 1})


def test_empty():
    _test_task((), {})


def test_single():
    _test_task({42}, {42: 1})


def test_types():
    _test_task((6, True, None, None, 1.0001, 1.0001, 'None', 6, 6),
               {True: 1, None: 2, 1.0001: 2, 'None': 1, 6: 3})
