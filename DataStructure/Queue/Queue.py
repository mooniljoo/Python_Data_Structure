# import queue

# data_queue = queue.Queue()

# data_queue.put("temp")
# data_queue.put(1)

# print(data_queue.qsize())
# print(data_queue.get())

# print(data_queue.qsize())
# print(data_queue.get())

queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


for index in range(10):
    enqueue(index)

dequeue()
print(len(queue_list))
