# Работа с деревьями

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def main():
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))

    if not numbers:
        print("Список пуст.")
        return

    tree = None
    for value in numbers:
        tree = insert(tree, value)

    print("Обход дерева в порядке возрастания:")
    inorder_traversal(tree)
    print()

if __name__ == "__main__":
    main()