#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['abC', 'aBc', 'ABC']

# Реализация задания 2
for item in Unique(data1):
    print(item)

print(list(Unique(data2)))
print(list(Unique(data3)))
