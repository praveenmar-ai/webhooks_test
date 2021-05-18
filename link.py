"""from  linkedlist import LinkedList 
def modify_linkedlist (input_stack):
    linkedlist = LinkedList()
    temp_stack = Stack(10)
    temp_queue = Queue(10)
    while not input_stack.is_empty():
        temp_stack.push(input_stack.pop())
        temp_queue.enqueue(input_stack.pop())
    while not input_stack.is_empty() and not (temp_queue.is_empty):
        linked_list.add (temp_stack.pop()+temp_stack.pop())
        linkedlist.add(temp_queue.dequeue()+temp_queue.dequeue())
    temp = linked_list.get_head()
    while temp.get_next() is not None:
        if (temp.get_data())%2==0:
            temp.set_data(temp.get_data()*2)
            
        else :
            temp.set_data(temp.get_next().get_data()*2)
        temp = temp.get_next()
    return linked_list

input_stack = 10,8,7,4,3,2,3,1
modify_linkedlist(input_stack)
"""
n1= 5
n2 = 4
while (n2>=1):
    print("*")
    for i in range (1,n1+1):
        print("*")
        n2  = n1 - 1
    print("8")
