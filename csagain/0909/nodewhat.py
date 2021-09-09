import sys
sys.setrecursionlimit(10**6)
pre = []
post= []
class Node:
    def __init__(self, data):
        self.x=data[0]
        self.y=data[1]
        self.value=data[2]
        self.lpar = None
        self.rpar = None
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.value)
class Tree:
    def __init__(self):
        self.root=None


    def preorder(self, node):
        pre.append(node.value)
        if node.left != None:
            self.preorder(node.left)
        if node.right != None:
            self.preorder(node.right)
    def postorder(self, node):
        if node.left != None:
            self.postorder(node.left)
        if node.right != None:
            self.postorder(node.right)
        post.append(node.value)
def makeTree(arr):
    a = arr.pop(0)
    lefts=[]
    rights=[]
    for x in arr:
        if x[0]<a[0]:
            lefts.append(x)
        else:
            rights.append(x)
    lefts.sort(key=lambda x:(-x[1],x[0]))
    a = Node(a)
    if lefts:
        a.left = makeTree(lefts)
    if rights:
        a.right = makeTree(rights)
    return a

def solution(nodeinfo):
    answer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    nodeinfo.sort(key=lambda x:(-x[1],x[0]))


    root= makeTree(nodeinfo)

    atree = Tree()
    atree.root= root



    atree.preorder(atree.root)
    atree.postorder(atree.root)
    answer= []
    answer.append(pre)
    answer.append(post)






    return answer