queue = []
# Enqueue desired values.
for i in range(1, 10):
    queue.append(i)

# Ask the user how many values should be swapped.
num_values_to_swap = int(input("How many values should be removed and placed on the back of the Queue: "))

for i in range(num_values_to_swap):
    temp = queue[0]
    del queue[0]
    print(temp)
    queue.append(temp)

print(queue)