'''
Method 1 (Use function to print a current level)

printLevelorder(tree):
1) getting height of tree
2) for d = 1 to height:
    printCurrentLevel(tree, d)

printCurrentLevel(tree, level):
    if tree is NULL return
    if level is 1, then
        print(tree -> data)
    else if level is greater than 1, then
        printCurrentLevel(tree->left, level)
        printCurrentLevel(tree->right, level)

Time Complexity? O(n^2) <- If tree is skewed, printCurrentLevel
takes O(n) times and printLevelOrder is O(n) + O(n-1) + ... O(1) which is O(n^2)
Space Complexity? O(n) <- printCurrentLevel() can use O(n)
'''
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)

# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

# Return height of input tree
def height(node):
    # If tree is empty
    if node is None:
        return 0
    else:
        # Calculate the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Return longer one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
printLevelOrder(root)
print(" ")

'''
Method 2 (Using queue)

printLevelorder(tree)
1) Create an empty queue q
2) temp_node = root /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node -> data
    b) Enqueue temp_node's children (first left then right children)
    c) Dequeue a node from q and assign it's value to temp_node

Time Complexity? O(n) <- n are the number of nodes in tree
Space Complexity? O(n) <- n are the number of nodes in tree (stored in queue)
'''

def printLevelOrder2(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level Order Traversal of binary tree is -")
printLevelOrder2(root)