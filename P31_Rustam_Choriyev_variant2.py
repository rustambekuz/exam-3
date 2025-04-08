# Exam - variant_2

# 1-Savol

def positive_args(func):
    def wrapper(*args):
       if any(arg<0 for arg in args):
           raise ValueError("Faqat musbat sondan iborat bo'lishi kerak!")
       print(func(*args))

    return wrapper

@positive_args
def multiply(a, b):
    return a * b

multiply(2, 3)
multiply(-1, 2)


# 2-Savol

import calendar
from datetime import datetime


def get_weekday(sana):
    date_sana=datetime.strptime(sana, '%Y-%m-%d')
    return calendar.day_name[date_sana.weekday()]


print(get_weekday("2023-10-25"))


# 3-Savol

from itertools import combinations
def cyclic_pairs(royxat):
    print(list(combinations(royxat,2)))

cyclic_pairs([1,2,3])


# 4-Savol

from dataclasses import dataclass

@dataclass()
class Product:
    name: str
    price:float
    quantity:int

    def total_cost(self):
        print(self.price * self.quantity)

p = Product(name="Apple", price=2.5, quantity=10)
p.total_cost()


# 5-Savol

from threading import Thread

def square_list(royxat):
    lst = []

    def func(item):
        a = item ** 2
        lst.append(a)

    for i in range(0, len(royxat)):
        thr = Thread(target=func, args=(royxat[i],))
        thr.start()
        thr.join()
    return lst

print(square_list([1, 2, 3, 4, 5]))
