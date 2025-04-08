import time
import asyncio
from asyncio import gather


# async def task1():
#     print("Task 1 started.")
#     await asyncio.sleep(2)
#     print("Task 1 done!")
#
# async def task2():
#     print("Task 2 started.")
#     await asyncio.sleep(1)
#     print("Task 2 done!")
#
# async def main():
#     await asyncio.gather(task1(),task2())
#
# asyncio.run(main())

# async def say1():
#     await asyncio.sleep(2)
#     print("Hello 1!")
#
# async def say2():
#     await asyncio.sleep(2)
#     print("Hello 2!")
#
# async def main():
#     tasks=(say1(),say2())
#     await asyncio.gather(*tasks)
#
# if __name__ == "__main__":
#     a=time.perf_counter()
#     asyncio.run(main())
#     b=time.perf_counter()-a
#     print(f"Dastur {b:.4f} secundda tugadi")


# lst=[1, 3, 2, 4, 4]
#
# from collections import Counter
# def second_largest(lst):
#     counts = Counter(lst)
#     return sorted(counts.items(),reverse=True)[1][0]
#
# print(second_largest(lst))


# parallel_sum([1, 2, 3, 4])
# Natija: 10

# from threading import Thread
# def parallel_sum(numbers):
#     total = [0, 0]
#     def sum_part(start, end, idx):
#         total[idx] = sum(numbers[start:end])
#
#     mid = len(numbers) // 2
#     t1 = Thread(target=sum_part, args=(0, mid, 0))
#     t2 = Thread(target=sum_part, args=(mid, len(numbers), 1))
#     t1.start(); t2.start()
#     t1.join(); t2.join()
#     return total[0] + total[1]
#
#
# print(parallel_sum([1, 2, 3, 4]))


# triple_list([1, 2, 3])
# Natija: [3, 6, 9]

# from multiprocessing import Process, Manager
# def triple_list(numbers):
#     manager = Manager()
#     results = manager.list([0] * len(numbers))
#     def triple(index, num):
#         results[index] = num * 3
#
#     processes = []
#     for i, num in enumerate(numbers):
#         p = Process(target=triple, args=(i, num))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#     return list(results)



# import asyncio
# async def divide_parallel(numbers):

# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(divide_parallel([2, 4, 6]))
# Natija: [1.0, 2.0, 3.0] (taxminan 0.5 sekundda)


# async def divide_parallel(numbers):
#     async def divide(x):
#         await asyncio.sleep(0.5)
#         return x / 2
#     results = await asyncio.gather(*[divide(num) for num in numbers])
#     return results


# Decorator bilan keshlash (10 ball)
# @cache_result
# def slow_multiply(a, b):
#     time.sleep(1)  # Simulyatsiya
#     return a * b
#
# slow_multiply(2, 3)  # 1 sekund kutadi, Natija: 6
# slow_multiply(2, 3)  # Darhol, Natija: 6

# def cache_result(func):
#     cache = {}
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     return wrapper


# from datetime import datetime
# from calendar import monthrange
# def last_day_of_month(year, month):
#     return monthrange(year, month)[1]





# from itertools import count
# def even_series():
#     for num in count(1):
#         yield num*2
#
# gen = even_series()
# num=[next(gen) for _ in range(3)]
# print(num)


# from datetime import datetime
# def hours_between(time1, time2):
#     t1 = datetime.strptime(time1, "%Y-%m-%d %H:%M")
#     t2 = datetime.strptime(time2, "%Y-%m-%d %H:%M")
#     return abs((t2 - t1).total_seconds() // 3600)



# from itertools import product
# def repeat_combinations(lst):
#     return list(product(lst, repeat=2))


# from dataclasses import dataclass
# @dataclass
# class Student:
#     name: str
#     age: int
#     grades: list
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)

#
# from enum import Enum
# class GameState(Enum):
#     START = 1
#     PLAYING = 2
#     END = 3
#
#     def prev_state(self):
#         return GameState(max(1, self.value - 1))







