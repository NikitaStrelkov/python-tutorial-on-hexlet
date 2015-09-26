__author__ = 'strelkov'
# ######
# task 2
# ######


def task(keys, vals):
    """
    Функция принимает два списка/кортежа ключей и значений:
    (k1, k2, ..., kn) и (v1, v2, ..., vm).

    Вернуть словарь вида {k1: v1, k2: v2, ...}.
    Если ключей больше чем значений, лишним ключам назначаются значения None.

    Примеры:
    >>> task(['a', 'b', 'c'], [1, 2, 3])
    {'a': 1, 'b': 2, 'c': 3}

    >>> task(['a', 'b', 'c', 'd', 'e'], [1, 2, 3])
    {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': None}
    """
    # BEGIN
    result = {}
    for i, key in enumerate(keys):
        try:
            val = vals[i]
            result[key] = val
        except:
            result[key] = None
    return result
    # END


def _test_task(seq1, seq2, expected):
    assert task(seq1, seq2) == expected


def test_ok():
    _test_task(['a', 'b', 'c'], [1, 2, 3], {'a': 1, 'b': 2, 'c': 3})


def test_extra_keys():
    _test_task(('a', 'b', 'c', 'd', 'e'), [1, 2, 3],
               {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': None})


def test_blank():
    _test_task((), [], {})
    _test_task((), [1, 2, 3], {})
