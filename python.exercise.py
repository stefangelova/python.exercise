def gen_nums(start, finish):
    numbers = []
    for i in range(start, finish + 1):
        if (i % 7 == 0) and (i % 5 != 0):
            numbers.append(str(i))
    return ','.join(numbers)
print(gen_nums(2000, 3200))
