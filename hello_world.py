from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()  
queue.popleft()   
print(queue)         


a = "Hello, World!"
print(a.upper())
print("gigione")