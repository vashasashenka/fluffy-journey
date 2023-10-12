import math


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1


    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            return

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def remove(self, index):
        if index >= self.size or index < 0:
            return
        current = self.head
        if index == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            for i in range(index):
                current = current.next
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def show(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    def show_size(self):
        print("Размер двусвязного списка = ", self.size)


class DynamicArray:
    def __init__(self, capacity):
        self.arr = []
        self.size = 0
        self.capacity = capacity

    def append(self, data):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size:self.size + 1] = [data]
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            return

        if self.size == self.capacity:
            self.resize()

        self.arr[index:index] = [data]
        self.size += 1

    def remove(self, index):
        if index >= self.size or index < 0:
            return
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.size - 1:self.size] = []
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        return self.arr[index]

    def show(self):
        for i in range(self.size):
            print(self.arr[i], end=' ')
        print()

    def show_size(self):
        print("Размер динамического массива = ", self.size)

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.capacity = new_capacity
        self.array = new_array


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack[len(self.stack):len(self.stack) + 1] = [data]

    def pop(self):
        if not self.is_empty():
            data = self.stack[-1]
            self.stack[len(self.stack) - 1:len(self.stack)] = []
            return data
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def show(self):
        for i in range(len(self.stack)):
            print(self.stack[i], end=' ')
        print()


def postfix(expression):
    op = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sin': 4, 'cos': 4}
    oper = Stack()
    post = []
    tokens = expression.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit():
            post.append(token)
        elif token in op:
            while not oper.is_empty() and oper.peek() != '(' and op[oper.peek()] >= op[token]:
                post.append(oper.pop())
            oper.push(token)
        elif token == '(':
            oper.push(token)
        elif token == ')':
            while not oper.is_empty() and oper.peek() != '(':
                post.append(oper.pop())
            oper.pop()
        elif token == 'sin' or token == 'cos':
            oper.push(token)
        i += 1
    while not oper.is_empty():
        post.append(oper.pop())
    return ' '.join(post)


def postfix_eval(expression):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        elif token == 'sin':
            x = stack.pop()
            stack.push(math.sin(x))
        elif token == 'cos':
            x = stack.pop()
            stack.push(math.cos(x))
        else:
            y = stack.pop()
            x = stack.pop()
            if token == '+':
                stack.push(x + y)
            elif token == '-':
                stack.push(x - y)
            elif token == '*':
                stack.push(x * y)
            elif token == '/':
                stack.push(x / y)
            elif token == '^':
                stack.push(x ** y)
    return stack.pop()


print("Двусвязный список: ")
dl = DoubleLinkedList()
dl.append(8)
dl.append(13)
dl.show()
dl.remove(1)
dl.show()
dl.prepend(26)
dl.insert(1, 10)
dl.show()
print(dl.get(1))
dl.show_size()

print("Динамический массив: ")
da = DynamicArray(13)
da.append(2)
da.append(6)
da.insert(1, 9)
print(da.get(0))
da.show()
da.remove(2)
da.show()
da.show_size()

print("Стек: ")
st = Stack()
st.push(5)
st.push(4)
st.push(15)
st.show()
st.pop()
st.show()
print(st.peek())

expression = input("Введите выражение: ")
print("Постфиксная форма:", postfix(expression), " = ", postfix_eval(postfix(expression)))  
