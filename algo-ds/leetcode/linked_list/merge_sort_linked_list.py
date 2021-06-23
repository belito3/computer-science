class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # push new value to linked lsit
    # using append method
    def append(self, new_value):

        # Allocate new node
        new_node = Node(new_value)

        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        # Append the new node at the end
        # of the linked list
        current_node.next = new_node

    def sortedMerge(self, a, b):
        result = None

        if a is None:
            return b
        
        if b is None: 
            return a

        if a.data < b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        
        middle = self.getMiddle(h)
        next_middle = middle.next

        middle.next = None

        left = self.mergeSort(h)
        right = self.mergeSort(next_middle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if (head == None):
            return head
        slow = fast = head

        while (fast.next is not None) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow

# Utility function to print the linked list
def printList(head):
    if head is None:
        print(' ')
        return
    
    current_node = head
    while current_node is not None:
        print(current_node.data, end = " ")
        current_node = current_node.next
    
    print(' ')

if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()

    l1.append(2)
    l1.append(3)
    #l1.append(4)
    l1.append(5)
    l1.append(6)

    l2.append(1)
    l2.append(2)
    l2.append(10)
    l2.append(15)

    l3 = l1.sortedMerge(l1.head, l2.head)
    printList(l3)

    li = LinkedList()

    # Let us create a unsorted linked list
    # to test the functions created
    # the list shall be a: 2 -> 3 -> 20 -> 5 -> 10 -> 15
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)

    # Apply merge Sort
    li.head = li.mergeSort(li.head)
    print("Sorted Linked List is: ")
    printList(li.head)