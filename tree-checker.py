class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this is all upside down to make declarations easier
root_1R_2L = Node(val=7)
root_1R_1L_1R = Node(val=47)
root_1R_1L = Node(val=22, left=root_1R_2L, right=root_1R_1L_1R)
root_2R_1L = Node(val=35)
root_3R = Node(val=1001)
root_2R = Node(val=107, left=root_2R_1L, right=root_3R)
root_1R = Node(val=50, left=root_1R_1L, right=root_2R)
root_1L_2R = Node(val=99)
root_1L_1R_1L = Node(val=20)
root_1L_1R = Node(val=45, left=root_1L_1R_1L, right=root_1L_2R)
root_2L_1R = Node(val=40)
root_3L = Node(val=1)
root_2L = Node(val=6, left=root_3L, right=root_2L_1R)
root_1L = Node(val=8, left=root_2L, right=root_1L_1R)
root = Node(val=36, left=root_1L, right=root_1R)

def fun7(node, value): # function name in assembly
    if (node == None):
        return -1
    
    node_value = node.val

    if (value < node_value):
        result = fun7(node.left, value)
        return result * 2
    elif (value > node_value):
        result = fun7(node.right, value)
        return result * 2 + 1
    else:
        return 0
    
if __name__ == "__main__":
    for i in range(0, 1001):
        if fun7(root, i) == 0:
            print(i)