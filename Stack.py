from No import No

class Stack: 
    def __init__(self):
        self.first = None
        self.size = 0

    def empty(self):
        if self.size == 0:
            return True
        return False

    def add(self, value):
        no = No(value)
        if self.empty():
            self.first = no
        else:
            aux = self.first
            self.first = no
            no.next = aux
        self.size += 1

    def print(self):
        if self.empty():
            print('Empty Stack')
        else:
            aux = self.first
            while(aux):
                print(str(aux.item))
                aux = aux.next
                
    def remove(self):
        if self.empty():
            print('Empty Stack')
        else:
            aux = self.first.next
            self.first = aux
            self.size -= 1

    def __len__(self):
        if self.empty():
            print('Empty Stack')
        else:
            print('Stacks contains {} itens'.format(str(self.size)))