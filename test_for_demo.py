# encoding='utf-8'

name = '1234567'

'''for ch in name:
    print(ch)'''

'''for index, every_char in enumerate(name):
    print(str(index) + ":" + every_char)'''

'''for every_char in iter(name):
    print(every_char)'''

'''numbers = [1, -3, 2, 9, 4, 7, 5]
new_numbers = sorted(numbers, reverse=True)
print(new_numbers)'''

# print(heapq.__all__)

from heapq import *

'''
heap = []
heappush(heap, 3)
heappush(heap, 2)
heappush(heap, 1)
print(heap) '''
'''
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
'''

'''heap = list(reversed(range(5)))
print("List", heap)
heapify(heap)
print("Heap:", heap)'''

'''heap = [5, 4, 3, 2, 1]
heapify(heap)
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))'''

'''from queue import PriorityQueue as PQueue

pq = PQueue()
pq.put((5 * -1, 'Python'))
pq.put((4 * -1, 'C'))
pq.put((3 * -1, 'Js'))
print("Inside PriorityQueue: ", pq.queue)  # 内部存储
while not pq.empty():
    print(pq.get()[1])'''

import random

'''lst = [random.randrange(1, 1000) for _ in range(5)]
lst.sort()
print("List: ", lst)
print("Poped: ", heappop(lst))
heappush(lst, 4)
print("Heap: ", lst)'''

'''heap = [random.randrange(1, 1000) for _ in range(50)]
heapify(heap)
print("N largest: ", nlargest(10, heap))
print("N smallest: ", nsmallest(10, heap))
print(len(heap))  # 不原地修改'''


