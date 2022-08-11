class Item:
    def __init__(self, item_name, status):
        self.item_name = item_name
        self.status = status


class ToDoList:
    # Class variable
    mylist = []

    def add_item(self, item):
        self.mylist.append(item)

    def remove_item(self, item_number):
        del self.mylist[item_number]

    def update_status(self, item_number, status):
        self.mylist[item_number].status = status

    def display(self):
        for i in range(len(self.mylist)):
            print()
            print("Item Number : ", i)
            print("item : ", self.mylist[i].item_name)
            print("status : ", self.mylist[i].status)
            print()

    def is_empty(self):
        if len(self.mylist) == 0:
            return True
        else:
            return False


while True:
    obj = ToDoList()
    print("Press 1 to add an item")
    print("Press 2 to remove an item")
    print("Press 3 to update status of item")
    print("Press 4 to display the items")
    print("Press 9 to quit")
    input_num = input("\nEnter Value : ")
    if input_num == "1":
        print("Enter Item name  : ")
        item_name = input()
        print("Enter Item status : ")
        status = input()
        input_item = Item(item_name, status)
        obj.add_item(input_item)

    if input_num == "2":
        if obj.is_empty():
            print("List is empty")
        else:
            obj.display()
            print("Enter item number to remove item ")
            inp = input()
            obj.remove_item(int(inp))

    if input_num == "3":
        if obj.is_empty():
            print("List is empty")
        else:
            obj.display()
            print("Enter item number to update status ")
            inp = input()
            print("Enter Updated Status")
            status = input()
            obj.update_status(int(inp), status)

    if input_num == "4":
        if obj.is_empty():
            print("List is empty")
        else:
            obj.display()

    if input_num == "9":
        break

    print()
