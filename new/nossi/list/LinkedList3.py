# 링크드리스트 => insert_back 구현
# 트리, 다른 자료구조 => 링크드 리스트 참고


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)