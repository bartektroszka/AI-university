#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import codecs


from copy import deepcopy
from queue import Queue

def list_to_int(l):
    val = 0
    for e in l[::-1]:
        val <<= 1
        val += e
    return val

#generuje wszystkie pozycje dla zadanego wzoru 
def generete_positions(n, pattern):
    if n <= 0:
        return [[]]
    if len(pattern) <= 0:
        return [[0] * n]

    seg_len = pattern[0]
    seg = [1] * seg_len
    m = n - seg_len

    if len(pattern) - 1 > 0:
        seg += [0]
        m -= 1
    positions = [seg + new_pattern for new_pattern in generete_positions(m, pattern[1:])]
    #obliczmy minimalny rozmiar wiersza/kolumny
    min_len = sum(pattern) + len(pattern) - 1
    if min_len < n:  
        return positions + [[0] + new_positions for new_positions in generete_positions(n - 1, pattern)]
    else:
        return positions

def reduce_columns(index, val, columns):
    prev_size = len(columns)
    columns[:] = [pattern for pattern in columns if pattern[index] == val]
    return prev_size != len(columns)

def reduce_rows(index, val, rows):
    prev_size = len(rows)
    rows[:] = [pattern for pattern in rows if pattern[index] == val]
    return prev_size != len(rows)


def AC_3(all_rows, all_columns):
    height, width = len(all_rows), len(all_columns)
    queue = Queue()

    for r in range(height):
        queue.put(('r', r))
    for c in range(width):
        queue.put(('c', c))

    while not queue.empty():
        orienatation, index = queue.get()
        
        if orienatation == "r":
            if len(all_rows[index]) == 0:
                return False

            ones = [min([row[i] for row in all_rows[index]]) for i in range(width)]
            zeros = [max([row[i] for row in all_rows[index]]) for i in range(width)]
            
            for i, (one, zero) in enumerate(zip(ones, zeros)):
                if one == 1:
                    reduced = reduce_columns(index, 1, all_columns[i])
                    if reduced: 
                        queue.put(("c", i))
                elif zero == 0:
                    reduced = reduce_columns(index, 0, all_columns[i])
                    if reduced: 
                        queue.put(("c", i))
        else: 

            if len(all_columns[index]) == 0: 
                return False

            ones = [min([col[i] for col in all_columns[index]]) for i in range(height)]
            zeros = [max([col[i] for col in all_columns[index]]) for i in range(height)]

            for i, (one, zero) in enumerate(zip(ones, zeros)):
                if one == 1:
                    reduced = reduce_rows(index, 1, all_rows[i])
                    if reduced: 
                        queue.put(("r", i))
                elif zero == 0:
                    reduced = reduce_rows(index, 0, all_rows[i])
                    if reduced: 
                        queue.put(("r", i))

    return True



def is_solved(all_rows, all_columns):
    return all([len(rc) == 1 for rc in all_rows + all_columns])

def find_unassigment_var(all_rows, all_columns):
    for y in range(len(all_rows)):
        if len(all_rows[y]) > 1:
            for x in range(len(all_rows[y][0])):
                if all_rows[y][0][x] != all_rows[y][1][x]:
                    return (y, x)

    for x in range(len(all_columns)):
        if len(all_columns[x]) > 1:
            for y in range(len(all_columns[x][0])):
                if all_columns[x][0][y] != all_columns[x][1][y]:
                    return (y, x)

    return None

def image(all_rows):
    return [row[0] for row in all_rows]

def find_image(rows, columns):
    height, width = len(rows), len(columns)

    stack = []

    all_rows = [generete_positions(width, row) for row in rows]
    all_columns = [generete_positions(height, column) for column in columns]

    AC_3(all_rows, all_columns)

    if is_solved(all_rows, all_columns):
        return image(all_rows)

    stack.append((all_rows, all_columns))

    while len(stack) > 0:
        all_rows1, all_columns1 = stack.pop()
        all_rows0, all_columns0 = deepcopy(all_rows1), deepcopy(all_columns1)

        if len(all_rows1) == 0 or len(all_columns1) == 0:
            continue
        (y, x) = find_unassigment_var(all_rows1, all_columns1)

        reduce_rows(x, 1, all_rows1[y])
        reduce_columns(y, 1, all_columns1[x])

        if AC_3(all_rows1, all_columns1):
            if is_solved(all_rows1, all_columns1):
                return image(all_rows1)
            stack.append((all_rows1, all_columns1))

        reduce_rows(x, 0, all_rows0[y])
        reduce_columns(y, 0, all_columns0[x])

        if AC_3(all_rows0, all_columns0):
            if is_solved(all_rows0, all_columns0):
                return image(all_rows0)
            stack.append((all_rows0, all_columns0))

    return None

IN_FILE = 'zad_input.txt'
OUT_FILE = 'zad_output.txt'
if __name__ == '__main__':
    with codecs.open(IN_FILE, 'r', 'utf8') as in_f, \
         codecs.open(OUT_FILE, 'w', 'utf8') as out_f:
        splited = in_f.read().split("\n")
        first_line = splited[0].split()
        h, w = int(first_line[0]), int(first_line[0])
        rows, columns = [], []

        for line in splited[1:h+1]:
            rows.append([int(n) for n in line.split()])

        for line in splited[h+1: -1]:
            columns.append([int(n) for n in line.split()])

        for line in find_image(rows, columns):
            out_f.write("".join(["#" if cell == 1 else "." for cell in line]))
            out_f.write("\n")
        pass
