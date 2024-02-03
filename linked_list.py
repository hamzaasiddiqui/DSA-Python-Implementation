class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print('List is empty')
            return
        
        i = self.head
        llstr = ''

        while i:
            if (i.next == None):
                llstr += str(i.data) + '-->None'
            else:
                llstr += str(i.data) + '-->'
            i = i.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        i = self.head

        while i.next:
            i = i.next

        i.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        length = 0
        i = self.head

        while i:
            length += 1
            i = i.next

        return length


    def remove_at(self, index):
        if index<0 or index>= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return

        i = self.head
        count = 0

        while i:
            if (count == index - 1):
                i.next = i.next.next
                break

            i = i.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        i = self.head
        count = 0

        while i:
            if (count == index - 1):
                node = Node(data, i.next)
                i.next = node
                break

            i = i.next
            count += 1


    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception('Linked list is empty!')
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        i = self.head
        while i:
            if i.data == data_after:
                i.next = Node(data_to_insert, i.next)
                break

            i = i.next


    def remove_by_value(self, data):
        if self.head is None:
            raise Exception('Linked list is empty!')
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        i = self.head
        while i.next:
            if i.next.data == data:
                i.next = i.next.next
                break

            i = i.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()