# DeQueue - Double Ended Queue // Can be inserted and popped by both ends

import collections

dQ = collections.deque(["Mon", "Tue", "Wed"])

dQ.append("Thu")

print(dQ)

print("Pop:", dQ.pop())
print("Pop:",dQ.popleft())