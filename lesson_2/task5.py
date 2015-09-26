__author__ = 'strelkov'


def task(distances):
    """
    Задание со звездочкой.

    Функция принимает последовательность расстояний.
    Каждое расстояние -- это список/кортеж вида (A, B, l), где:
    A -- строка, имя пункта A;
    B -- строка, имя пункта B;
    l -- положительное число, расстояние между A и B.

    Вернуть словарь, который хранит расстояния
    как между A и B, так и между B и A.

    Пример:
    >>> result = task((
        ('Oslo', 'Chita', 234),
        ('London', 'Astana', 743),
    ))
    >>> result['Oslo']['Chita']    # 234
    >>> result['Chita']['Oslo']    # 234
    >>> result['London']['Astana'] # 743
    >>> result['Astana']['London'] # 743
    """
    # BEGIN
    result = {}
    for city_from, city_to, length in distances:

        if city_from not in result:
            result[city_from] = {}
        result[city_from][city_to] = length

        if city_to not in result:
            result[city_to] = {}

        result[city_to][city_from] = length

    return result
    # End


def _test_task(distances, expected):
    result = task(distances)
    for (a, b, l) in distances:
        assert result[a][b] == l
        assert result[b][a] == l


def test_ok():
    _test_task(
        [
            ('A', 'B', 2),
            ('A', 'C', 3),
            ('B', 'C', 4),
        ],
        {
            'A': {'B': 2, 'C': 3},
            'B': {'A': 2, 'C': 3},
            'C': {'A': 3, 'B': 4},
        }
    )


def test_empty():
    _test_task([], {})


def test_single():
    _test_task([['Moscow', 'London', 1234.5]], {
        'Moscow': {'London': 1234.5},
        'London': {'Moscow': 1234.5},
    })