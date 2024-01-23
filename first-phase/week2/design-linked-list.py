class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self. size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        current_node = self.head.next
        for i in range(index):
            current_node = current_node.next    
        return current_node.value
   
   

    def addAtHead(self, val: int) -> None:
        current_node = self.head.next
        newNode = Node(val)
        self.head.next = newNode
        self.head.next.next = current_node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        current_node = self.head
        while current_node.next is not None:
            current_node= current_node.next
        newNode = Node(val)
        current_node.next = newNode
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        current_node = self.head
        newNode = Node(val)
        temp1 = Node(0)
        for i in range(0,index):
            current_node = current_node.next
        temp1 = current_node.next
        current_node.next=newNode
        current_node.next.next = temp1
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        current_node = self.head
        for i in range(0,index):
            current_node = current_node.next
        temp1 = Node(0)
        temp1 = current_node.next
        current_node.next = temp1.next
        temp1.next = None
        self.size-=1
        del temp1
        
       


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


