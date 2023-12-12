class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self):
        pass
    
    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

my_linked_list = LinkedList(4)
my_list = my_linked_list.head.value

print(my_list)