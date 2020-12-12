#Using Lists as Queues
from collections import deque
color_list = deque(["Red", "Blue", "Green", "Black"])
color_list.append("White")      # White arrive
print(color_list)
# deque(['Red', 'Blue', 'Green', 'Black', 'White'])
color_list.append("Yellow")     # Yellow arrive
print(color_list)
#deque(['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow'])
color_list.popleft()            # The first to arrive now leaves 'Red'
print(color_list)
#deque(['Blue', 'Green', 'Black', 'White', 'Yellow'])
color_list.popleft()            # The second to arrive now leaves 'Blue'
print(color_list)
#deque(['Green', 'Black', 'White', 'Yellow'])
print(color_list)               # Remaining queue in order of arrival
#deque(['Green', 'Black', 'White', 'Yellow'])