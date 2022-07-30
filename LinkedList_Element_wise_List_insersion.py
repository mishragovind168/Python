#3
#Linked List delete element at index
#insert List element in LinkedList

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data,None)
    
    def insert_List(self,data):
        
        if self.head ==None:
            for i in data:
                self.insert_at_end(i)
        else:
            temp = self.head
            while temp:
                temp = temp.next
            for i in data:
                self.insert_at_end(i)
            
                
    
    def print(self):
        if self.head is None:
            print("Empity List")
            
        else:
            temp = self.head
            while temp:
                print(temp.data,end='--> ')
                temp = temp.next
    
    
    
obj = LinkedList()
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.insert_List([9,2,3,4,5,6])
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.print()
                
  
 # output:  1--> 2--> 3--> 9--> 2--> 3--> 4--> 5--> 6--> 1--> 2--> 3--> 
