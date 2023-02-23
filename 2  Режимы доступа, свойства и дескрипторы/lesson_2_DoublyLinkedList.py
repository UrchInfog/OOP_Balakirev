class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


class DoublyLinkedLst:
    def __init__(self):
        self.node_start = None
        self.node_end = None

    def check_node_start(self, data):
        if self.node_start is None:
            node_new = Node(data)
            self.node_start = node_new
            return False
        else:
            return True

    def insert_start(self, data):
        if self.check_node_start(data):
            node_new = Node(data)
            node_new.next = self.node_start
            self.node_start.prev = node_new
            self.node_start = node_new

    def insert_end(self, data):
        if self.check_node_start(data):
            node_new = Node(data)
            if self.node_end != None:
                node_end = self.node_end
            else:
                node_end = self.node_start
                while node_end.next != None:
                    node_end = node_end.next
            node_end.next = node_new
            node_new.prev = node_end
            self.node_end = node_new

    def print_lst(self):
        if self.node_start:
            obj = self.node_start
            while obj != None:
                print(obj.item)
                obj = obj.next


lst = ("Люблю отчизну я, но странною любовью!", "Не победит ее рассудок мой.", "Ни слава, купленная кровью,")

dbl = DoublyLinkedLst()
dbl.insert_start(lst[0])
dbl.insert_start(lst[1])
dbl.insert_start(lst[2])

dbl.print_lst()

# print(dbl.node_start.item)
# print(dbl.node_start.next.item)
# print(dbl.node_start.next.next.item)

dbl1 = DoublyLinkedLst()
dbl1.insert_end(lst[0])
dbl1.insert_end(lst[1])
dbl1.insert_end(lst[2])

# print(dbl1.node_start.item)
# print(dbl1.node_start.next.item)
# print(dbl1.node_start.next.next.item)
dbl1.print_lst()