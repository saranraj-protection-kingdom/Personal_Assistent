class stackoperation:
    def __init__(self):
        self.stack = []
        maxsize=10
        top=-1
    def push_the_element_in_stack(self,value):
        if (top==maxsize):
            print ("Stack is full")
        else:
            top=top+1
            stack[top]=value
    def pop_the_element_in_stack():
        if (top==-1):
            print ("Stack is empty")
        else:
            data=stack[top]
            top=top-1
            print (data+ " the element has been deleted")
    # def display_the_stack_element():
    #     for i in range (0,len(stack)):
    #         print stack[i]


s=stackoperation()
s.push_the_element_in_stack(1)
s.push_the_element_in_stack(2)
s.push_the_element_in_stack(3)
s.push_the_element_in_stack(4)
s.push_the_element_in_stack(5)
s.push_the_element_in_stack(6)
s.push_the_element_in_stack(7)
s.pop_the_element_in_stack()
s.pop_the_element_in_stack()
# s.display_the_stack_element()c
