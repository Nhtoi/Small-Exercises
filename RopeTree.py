LEAF_LEN = 32

class Rope():
    def __init__(self):
        self.length = None
        self.data = [0] * (LEAF_LEN + 1)
        self.right = None
        self.left = None
        self.lCount = None
    
def CreateTreeRope(node, par, a, l ,r):
    tmp = Rope()
    tmp.left = tmp.right = None
    tmp.parent = par

    if (r-l) > LEAF_LEN:    
        tmp.data = None
        tmp.lCount = (r-l) // 2
        node = tmp
        m = (l + r) // 2
        tmp.left = CreateTreeRope(tmp.left, tmp, a, l, m)
        tmp.right = CreateTreeRope(tmp.right, tmp, a, m + 1, r)
    else:
        node = tmp
        tmp.lCount = (r-l)
        j = 0
        for i in range(l,  r + 1):
            print(a[i], end="")
            tmp.data[j] =a [i]
            j = j + 1
        print(end = "")
    return node

def printdataing(r):
    if r == None:
        return 
    if r.left == None and r.right == None:
        pass
    printdataing(r.left)
    printdataing(r.right)


def Concatenate(root3, root1, root2, n1):
    tmp = Rope()
    tmp.left = root1
    tmp.right = root2
    root1.parent = tmp
    root2.parent = tmp
    tmp.lCount = n1
    tmp.data = None
    root3 = tmp
    return root3


root1 = None
a =  "Hi This is geeksforgeeks. "
n1 = len(a)
root1 = CreateTreeRope(root1, None, a, 0, n1-1)

# Create a Rope tree for second dataing
root2 = None
b =  "You are welcome here."
n2 = len(b)
root2 = CreateTreeRope(root2, None, b, 0, n2-1)

# Concatenate the two dataings in root3.
root3 = None
root3 = Concatenate(root3, root1, root2, n1)

# Print the new concatenated dataing
printdataing(root3)
print()

# The code is contributed by Nidhi goel.
    