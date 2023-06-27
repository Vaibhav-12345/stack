class Stack:
    def __init__(self, size):
        self.maxlen = size
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        if self.top==self.maxlen-1:
            return True
        return False


    def push(self, item):
        if self.is_full():
            print("Stack Overflow: Cannot push item.")
        else:
            self.stack.append(item)
            self.top += 1

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Cannot pop item.")
        else:
            item = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return item

    def peek(self):
        if self.is_empty():
            print("Stack Underflow: Stack is empty. Cannot peek item.")
        else:
            return self.stack[self.top]

    def size(self):
        return self.top + 1


st = Stack(5)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(6)
st.push(7)
print(st.stack)

# st.pop()
# st.pop()
# st.pop()
# st.pop()

# print(st.stack)
