class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def getPath(root, path, key):
    if root == None:
        return False
    path.append(root.key)

    if root.key == key:
        return True
    
    if ((root.left != None and getPath(root.left, path, key)) or
            (root.right!= None and getPath(root.right, path, key))):
        return True

    path.pop()
    return False

def getLCA(root, node1, node2):
    path1 = []
    path2 = []

    if (not getPath(root, path1, node1) or not getPath(root, path2, node2)):
        return -1
    
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print ("LCA(4, 5) = %d" %(getLCA(root, 4, 5)))
print ("LCA(4, 6) = %d" %(getLCA(root, 4, 6)))
print ("LCA(3, 4) = %d" %(getLCA(root,3,4)))
print ("LCA(2, 4) = %d" %(getLCA(root,2, 4)))