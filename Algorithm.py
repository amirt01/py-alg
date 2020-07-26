"""
 Name: Amir Tadros
 Date: 7/26/2020
 Purpose: Port all of the c++17 and older Algorithms from the c++ Algorithm Library to Python in order
          to learn more about Python and practice writing some simple algorithms.
"""


def all_of(iterable, predicate):
    for index in iterable:
        if not predicate(index):
            return False
    return True


def any_of(iterable, predicate):
    for index in iterable:
        if predicate(index):
            return True
    return False


def none_of(iterable, predicate):
    for index in iterable:
        if predicate(index):
            return False
    return True


def for_each(iterable, predicate):
    return [predicate(index) for index in iterable]


def for_each_n(iterable, start, end, predicate):
    return [predicate(index) for index in iterable[start:end]]


def count(iterable, value):
    counter = 0
    for index in iterable:
        if index == value:
            counter += 1
    return counter


def count_if(iterable, predicate):
    counter = 0
    for index in iterable:
        if predicate(index):
            counter += 1
    return counter


def mismatch(iterable1, iterable2):
    i = 0
    while i < len(iterable1) - 1 and i < len(iterable2) - 1 and iterable1[i] == iterable2[i]:
        i += 1
    return iterable1[i], iterable2[i]


def find(iterable, value):
    i = 0
    while i < len(iterable) - 1 and iterable[i] != value:
        i += 1
    return i


def find_if(iterable, predicate):
    i = 0
    while i < len(iterable) and not predicate(iterable[i]):
        i += 1
    return i


def find_if_not(iterable, predicate):
    i = 0
    while i < len(iterable) and predicate(iterable[i]):
        i += 1
    return i


def find_end(iterable, predicate):
    i = len(iterable) - 1
    while i > 0 and not predicate(iterable[i]):
        i -= 1
    return i
