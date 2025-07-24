# Last In First Out (LIFO) - Stack Implementation


stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

stack.append(11)  # Add to the end of the stack
print(stack)
stack.append(12)  # Add to the end of the stack
print(stack)

stack.pop()  # Remove the last element
print(stack)

# First In First Out (FIFO) - Queue Implementation

from collections import deque

queue = deque()
queue.append(1)  # Add to the end of the queue
queue.append(2)  # Add to the end of the queue
queue.append(3)  # Add to the end of the queue
queue.popleft()  # Remove the first element
print(queue)