__author__ = 'strelkov'


def task(func, *seq):
    """
    The function receives a function and N sequences (lists/tuples).
    All sequences have the same length M.
    The number of arguments of the func is equal to the number of sequences.
    Return a list of [res1, res2, ..., resM], where:

    res1 = func(seq1[1], seq2[1], ..., seqN[1])
    res2 = func(seq1[2], seq2[2], ..., seqN[2])
    ...
    resM = func(seq1[M], seq2[M], ..., seqN[M])
    """
    res = []
    for i, seq_value in enumerate(seq):
        print(i)
        print(seq_value)
        res.append(func())

task(12, [1, 2], [1, 2], [1, 2], [1, 2])
