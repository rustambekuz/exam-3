
# async def task1():
#     print("task1 ishlayapti")
#     await asyncio.sleep(2)
#     print("task1 tugadi")
#
#
# async def task2():
#     print("task2 ishlayapti")
#     await asyncio.sleep(2)
#     print("task2 tugadi")
#
# async def main():
#     tasks=(task1(),task2())
#     await asyncio.gather(*tasks)

# if __name__=='__main__':
#     a = time.perf_counter()
#     asyncio.run(main())
#     b = time.perf_counter() - a
#     print(f"{b:.4f} secundda tugadi")


# import time
# import asyncio
#
# async def task1(name,timer):
#     print(f"{name} ishladi")
#     await asyncio.sleep(timer)
#     print(f"{name} tugadi")
#
# async def main():
#     tasks=[
#         asyncio.create_task(task1('A',timer=1)),
#         asyncio.create_task(task1('B',timer=2)),
#         asyncio.create_task(task1('C',timer=3)),
#         asyncio.create_task(task1('D',timer=4)),
#     ]
#
#     dones,pending =await asyncio.wait(tasks,timeout=3)
#     print("bajarildi")
#
#     for done in dones:
#         print(f"{done.get_name()}:{done.result()}")
#
#     print('vaqt tugadi')
#
# if __name__=='__main__':
#     asyncio.run(main())

# import asyncio
# async def task1():
#     print("Task1: start")
#     await asyncio.sleep(2)
#     print("Task1: done")
#
# async def task2():
#     print("Task2: start")
#     await asyncio.sleep(1)
#     print("Task2: done")
#
# async def main():
#     await asyncio.gather(task1(), task2())
#
# asyncio.run(main())

# import asyncio
#
# async def say_hello():
#     print("Salom!")
#     await asyncio.sleep(1)
#     print("Hello!")
#
# async def say_goodbye():
#     print("Xayr!")
#     await asyncio.sleep(2)
#     print("Goodbye!")
#
# async def main():
#     await asyncio.gather(say_hello(), say_goodbye())
#
# asyncio.run(main())


# import asyncio
#
# async def get_number():
#     await asyncio.sleep(2)
#     print(42)
#
# async def get_word():
#     await asyncio.sleep(3)
#     print('Hisob kitob tugadi!')
#
# async def main():
#     await asyncio.gather(get_number(),get_word())
# asyncio.run(main())

# import asyncio
#
# async def func(task_id):
#     print(f"Task {task_id} boshlandi..")
#     await asyncio.sleep(task_id)
#     print(f"Task {task_id} tugadi.")
#
#
# async def main():
#     tasks=[func(i) for i in range(1,5)]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())



# import asyncio
# import random
#
# async def download_file(file_name):
#     download_time = random.randint(1, 5)
#     print(f"{file_name} yuklanmoqda ({download_time} soniya)...")
#     await asyncio.sleep(download_time)
#     print(f"{file_name} yuklandi!")
#
# async def main():
#     files = ["file1.txt", "file2.txt", "file3.txt"]
#     tasks = [download_file(file) for file in files]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())


# import asyncio
#
# async def multiply(a, b):
#     await asyncio.sleep(2)
#     return a * b
#
# async def main():
#     results = await asyncio.gather(
#         multiply(3, 4),
#         multiply(7, 2),
#         multiply(5, 6)
#     )
#     print("Natijalar:", results)
#
# asyncio.run(main())

# dekorator yaratish
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Funksiya chaqirilishdan oldin")
#         func(*args, **kwargs)
#         print("Funksiya chaqirilishdan keyin")
#
#     return wrapper
# @my_decorator
# def hi():
#     print("hello,world")
#
#
# hi()

# def add_number(func):
#     def wrapper(*args, **kwargs):
#         print("funksiya boshlandi..")
#         result = func(*args, **kwargs)
#         print("funksiya tugadi")
#         return result
#     return wrapper
# @add_number
# def add(a, b):
#     return a + b
#
# print(add(2, 3))


# def add(a,b):
#     return a+b
#
# add_number=lambda a,b: a+b
# print(add(1,2))
# print(add_number(1,2))

# numbers=[1,2,3,4,5]
# a=map(lambda x:x*2,numbers)
# print(list(a))

# import copy
# class MyClass:
#     def __init__(self,value):
#         self.value = value
#         self.inner=[1,2,3]
#
#     def __copy__(self):
#         return MyClass(self.value)
#
# obj1=MyClass(10)
# obj2=copy.copy(obj1)
#
# obj2.inner[0]=99
# print(obj1.inner)


import copy
from importlib import import_module

# list1=[[1,2],[3,4]]
# list2=copy.copy(list1)
# list2[0][0]=99
# print(list1)
# print(list2)

# list1=[[1,2],[3,4]]
# list2=copy.deepcopy(list1)
# list2[0][0]=99
# print(list1)
# print(list2)


# def generator():
#     n=1
#     while True:
#         yield n
#         n+=1
#
# gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# import asyncio
# import time
#
# def task_sync(x):
#     print(f"Task sync: {x} working")
#     time.sleep(2)
#     print(f"Task sync: {x} done")
# task_sync('example 1')
#
# print('-'*72)
#
# async def task_async(x):
#     print(f"Task async: {x} working")
#     await asyncio.sleep(2)
#     print(f"Task async: {x} done")
#
# tasks=(task_async('example 2'),task_async('example 3'))
#
# async def main():
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())

# import asyncio
#
# async def main():
#     print("Hello...")
#     await asyncio.sleep(1)
#     print("...World")
#
# asyncio.run(main())


# https://ballistic-archer-6c3.notion.site/Variant-2-1cfd424035c180feb902c14b4ce2b9a2


# Variant-2-1cfd424035c180feb902c14b4ce2b9a2








