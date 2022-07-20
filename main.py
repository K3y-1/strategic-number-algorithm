import random, math, time

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.left_count = 0 

class  BST:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, val):
        n = self.root
        s = 0
        while 1:
            if val > n.value:
                s += n.left_count + 1
                if not n.right:
                    n.right = Node(val)
                    return s
                n = n.right
            else:
                n.left_count += 1
                if not n.left:
                    n.left = Node(val)
                    return s
                n = n.left

def timer(func):
    def wraper(*args):
        t = time.time()
        print(func(*args))
        print(f'{func.__name__} total time: {time.time() - t}')
    return wraper

@timer
def binary_tree_strategic_num(arr):
    t = BST(arr[-1])
    strategic_num = 0
    for i in arr[-2::-1]:
        strategic_num += t.insert(i)
    return strategic_num

if __name__ in "__main__":
    r = [random.randint(1, 100000) for i in range(1000000)]
    binary_tree_strategic_num(r)