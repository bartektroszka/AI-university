def opt_dist(array, D):
    array = list(array)
    for i in range(len(array)):
        array[i] = int(array[i])
    options = []
    for i in range(len(array) - D + 1):
        number_of_ones_inside = 0
        number_of_ones = 0
        for j in range(D):
            if array[i+j] == 1:
                number_of_ones_inside += 1
        for j in range(len(array)):
            if array[j] == 1:
                number_of_ones += 1
        options.append(D - number_of_ones_inside + number_of_ones - number_of_ones_inside)

    return min(options)

print(opt_dist("0010001000", 5))
print(opt_dist("0010001000", 4))
print(opt_dist("0010001000", 3))
print(opt_dist("0010001000", 2))
print(opt_dist("0010001000", 1))
print(opt_dist("0010001000", 0))

