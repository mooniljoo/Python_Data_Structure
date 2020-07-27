# 객체지향
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        # 비어있는 경우
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return

        # head를 삭제하는 경우
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp

        # 마지막 Node 삭제하는 경우
        # 중간 Node 삭제하는 경우
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next


linkedlist1 = NodeMgmt(0)
print(linkedlist1.desc())
print(linkedlist1.head)
linkedlist1.delete(0)
print(linkedlist1.desc())
print(linkedlist1.head)

linkedlist1 = NodeMgmt(0)
print(linkedlist1.desc())
for data in range(1, 10):
    linkedlist1.add(data)
print(linkedlist1.desc())

linkedlist1.delete(3)
print(linkedlist1.desc())
