import csv
import itertools

with open('Data/data.csv') as file:
    reader, length = itertools.tee(csv.reader(file, delimiter=','))
    l = int((len(next(length)) - 1) / 25)
    del length
    for row in reader:
        for i in range(l):
            print(f'x value of {i} is: {row[(25 * i) + 4]} light years')
            print(f'y value of {i} is: {row[(25 * i) + 5]} light years')