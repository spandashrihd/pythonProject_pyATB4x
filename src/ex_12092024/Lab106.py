#deque: list like sequence
from collections import deque

#d=dequeue()
d=deque([2,3,5])
print(d)

#append to deque
d.append(4)
print(d)

#add element to left end
d.appendleft(0)
print(d)

#extend the deque element
d.extend([10,7,8])
print(d)

#extend the deque element at left
d.extendleft([100,300,800])
print(d)

#pop
print(d.pop())

#pop the starting element
print(d.popleft())