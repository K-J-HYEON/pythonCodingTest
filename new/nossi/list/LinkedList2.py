class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6

# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#     def append(self, value):
#         new_node = Node(value)
#         self.head = new_node

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# 중간 인덱스에 노드를 추가하는것 => insert_at(idx, value)
# remove로 제거하려는 인덱스 삭제 => 가비지 컬렉터가 쓰지 않는 노드 삭제
# 삽입 삭제 링크드 리스트 코드 구현
# insert_back


