class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # ----- LECTURE METHODS -----
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
    def search(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    # ----- LABORATORY METHODS -----
    def remove_at_beginning(self):
        if self.head == None:
            return

        removed_data = self.head
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        removed_data.next = None

        print(f"Removed data at beginning: {removed_data.data}")
        return removed_data.data

    def remove_at_end(self):
        if self.tail == None:
            return
        
        if self.head == self.tail:
            removed_data = self.tail
            self.head = None
            self.tail = None
            return
        
        current_node = self.head

        while current_node:
            if current_node.next == self.tail:
                removed_data = self.tail
                self.tail = current_node

                self.tail.next = None
                removed_data.next = None

                break
            else:
                current_node = current_node.next
        
        print(f"Removed data at end: {removed_data.data}")
        return removed_data.data

    def remove_at(self, data):
        if self.head.data == data:
            self.remove_at_beginning()
            return

        if self.tail.data == data:
            self.remove_at_end()
            return

        previous_node = self.head
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                removed_data = current_node

                previous_node.next = current_node.next
                current_node.next = None

                print(f"Removed data: {removed_data.data}")
                return removed_data.data

            previous_node = current_node
            current_node = current_node.next
        
        print(f"{data} not found")

    # ----- EXTRA METHODS -----
    def insert_at(self, data, data_location):
        new_node = Node(data)
        current_node = self.head
        
        while current_node:
            if current_node.data == data_location:
                if self.tail == current_node:
                    self.tail = new_node

                new_node.next = current_node.next
                current_node.next = new_node

                break
            else:
                current_node = current_node.next

    def get_linked_list(self):
        linked_list = []
        current_node = self.head

        while current_node:
            linked_list.append(current_node.data)
            current_node = current_node.next
        
        return linked_list
    
    def get_linked_list_size(self):
        return len(self.get_linked_list())


if __name__ == "__main__":
    linked_list = LinkedList()

    # Adding elements
    linked_list.insert_at_end("Banana")
    linked_list.insert_at_beginning("Orange")
    linked_list.insert_at_beginning("Strawberry")
    linked_list.insert_at_end("Mango")
    linked_list.insert_at("Pineapple", "Banana")

    print(linked_list.get_linked_list())

    # Search
    print(linked_list.search("Banana"))
    print(linked_list.search("Bann"))
    print(linked_list.search("Mango"))
    print(linked_list.search("Kiwi"))
    print(linked_list.search("Straberry")
)
    # Removing elements
    linked_list.remove_at_beginning()
    print(linked_list.get_linked_list())

    linked_list.remove_at_end()
    print(linked_list.get_linked_list())

    linked_list.remove_at_beginning()
    print(linked_list.get_linked_list())

    linked_list.remove_at("Banana")
    print(linked_list.get_linked_list())
