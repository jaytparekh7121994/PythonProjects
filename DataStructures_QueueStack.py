from collections import deque

queue = deque(["Eric", "Chagan", "Magan", "Michael"])
print(queue)
queue.append("Terry")
queue.append("Ferry")
print(queue)

for i in range(len(queue)):
    print(queue.popleft())

print("queue=", queue)

stack = list([3, 4, 5])
print(stack)
stack.append(6)
stack.append(7)
print(stack)

for i in range(len(stack)):      # if you use range(stack) : 7,6,5 is output
    print(stack.pop())
print("stack=", stack)
