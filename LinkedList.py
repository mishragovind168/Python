#2
#Linked List Implentation

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

# Insert element at end            
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data,None)
            
# Insert element at start    
    def insert_start(self,data):
        if self.head is None:
            self.head = Node(data,None)
        else:
            node = Node(data,self.head)
            self.head = node
            
    def delete_first(self):
        if self.head is None:
            print("LinkList is emPity")
        else:
            self.head.data = None
            
    
#Print function            
    def print(self):
        if self.head is None:
            print("LinkedList is empity")
            
        else:
            temp = self.head
            lstr = ''
            while temp is not None:
                lstr+= str(temp.data)+'--> '
                temp = temp.next

            print(lstr)
            
obj = LinkedList()
obj.insert_start(1)
obj.insert_start(4)
obj.insert_end(45)
obj.print()
obj.delete_first()
obj.print()


'''
Output
4--> 1--> 45--> 
None--> 1--> 45-->

'''
