from Stack import Stack

stack = Stack()
menu = '''
+˜˜˜˜˜˜˜˜MENU˜˜˜˜˜˜˜˜+
|   1 - Add          |
|   2 - Print        |
|   3 - Remove       |
|   4 - Size         |
|   5 - Exit         |
+˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜+
Choose an option: '''

while True:
    option = (input(menu))

    if option == '1':
       stack.add(input('Enter a value: '))
    elif option == '2':
        stack.print()   
    elif option == '3':
        stack.remove()
    elif option == '4':
        stack.__len__()   
    elif option == '5':
        break
    else:
        print('Invalid option. Try again.')