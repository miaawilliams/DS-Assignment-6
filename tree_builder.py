class EmployeeNode:
    def __init__(self, value, name=None):
        self.value = value
        self.name = name
        self.left = None
        self.right = None

root = EmployeeNode("Ceo")
manager_1 = EmployeeNode("Lisa")
manager_2 = EmployeeNode("Greg")
employee_1 = EmployeeNode("Lauren")
employee_2 = EmployeeNode("Jacob")
employee_3 = EmployeeNode("Andrew")
employee_4 = EmployeeNode("Maddie")

root.left = manager_1
root.right = manager_2

manager_1.left = employee_1
manager_1.right = employee_2

manager_2.left = employee_3
manager_2.right = employee_4


# print(root.left.right.value)

class TeamTree: 
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Tree is empty.")
            return False
        if current_node is None:
            current_node = self.root
        
        if current_node.value == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = EmployeeNode(employee_name)
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = EmployeeNode(employee_name)
                return True
            else:
                print("No more sides available")
                return False
            
        if current_node.left:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True
        if current_node.right:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True
            
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is None:
            print("No team lead added yet")
            return
        
        print("   " * level + f"- {node.value}")
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)

'''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

company_directory = TeamTree()
company_directory.root = root    



# # CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


company_directory()




# Instead of writing countless loops to find each manager or employee and their whereabouts, recursion just goes down the tree to find the name
# until it returns true and can add in the inserted value. Instead of taking a big problem head on, it simplifies the big problem into smaller, 
# more managable problems to work through. Rather than finding a specific manager or employee throughout the whole tree, it cycles through 
# returning false until it finds the match and returns true. When finding a spot for an employee, you can't just place it anywhere. The 
# biggest problem is placing it with the right manager in either the right or left spot. Unlike previous data structures, I couldn't just 
# use an 'insert' function or an .add and place it in. I had to make sure my code was correctly checking the values in the tree and placing
# it with the corret manager. Trees are better for example problems like these- where a hierarchy system is needed. The values within trees
# depend on each other. Other data structures, like lists, are good for keeping in order or sequence, but are not reliable for looking
# up things quickly, or allowing for a hiearchy system. Along with sets, its values don't depend on one another, however; they are good for 
# faster lookup times. 