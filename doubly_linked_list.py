class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)
        else:
            self.head.prev = Node(data, self.head, None)
            self.head = self.head.prev

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        i = self.head

        while i.next:
            i = i.next

        i.next = Node(data, None, i)


    def print_forward(self):
        if self.head is None:
            print('Linked list empty!')
            return
        
        i = self.head
        llstr = 'None<-->'

        while i:
            if (i.next == None):
                llstr += str(i.data) + '<-->None'
            else:
                llstr += str(i.data) + '<-->'
            i = i.next

        print(llstr)


    def get_last_node(self):
        i = self.head

        while i.next:
            i = i.next

        return i

    def print_backward(self):
        if self.head is None:
            print('Linked list is empty!')
            return
        
        last_node = self.get_last_node()
        i = last_node
        llstr = 'None<-->'

        while i:
            if (i.prev == None):
                llstr += str(i.data) + '<-->None'
            else:
                llstr += str(i.data) + '<-->'
            i = i.prev

        print(llstr)

    def get_length(self):
        count = 0
        i = self.head

        while i:
            count += 1
            i = i.next

        return count
    
    def insert_at(self, index, data):
        if index > 0 or index > self.get_length():
            raise Exception('Invalid index!')
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        i = self.head
        while i:
            if count == index - 1:
                node = Node(data, i.next, i)
                if node.next:
                    node.next.prev = node
                i.next = node
                break

            i = i.next
            count += 1


    def remove_at(self, index, data):
        if index > 0 or index > self.get_length():
            raise Exception('Invalid index!')
            return
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        i = self.head

        while i:
            if count == index:
                i.prev.next = i.next
                if i.next:
                    i.next.prev = i.prev
                break

            i = i.next
            count += 1

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)



if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()