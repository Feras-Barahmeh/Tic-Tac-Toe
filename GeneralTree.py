
class TreeNode:
    def __init__(self, board):
        self.board = board
        self.childes = []
        self.parent = None
        self.status = None


    def addChild(self, child):
        child.parent = self
        self.childes.append(child)

    def displayTree(self):
        indentation = ' ' * self.getLevel * 3
        path = indentation + f"{self.getLevel} |----->> " if self.parent else '-- Root -- '
        print(path , self.board)
        if self.childes:
            for child in self.childes:
                child.displayTree()

    @property
    def getLevel(self):
        level = 0
        grandson = self.parent
        while grandson:
            level += 1
            grandson = grandson.parent
        return level


def createTree():
    root = TreeNode("Electronics")

    laptops = TreeNode("Laptops")
    laptops.addChild(TreeNode("MacBook"))
    laptops.addChild(TreeNode("lenovo"))
    laptops.addChild(TreeNode("HP"))

    phonec = TreeNode("Laptops")
    phonec.addChild(TreeNode("MacBook"))
    phonec.addChild(TreeNode("lenovo"))
    phonec.addChild(TreeNode("HP"))

    televegin = TreeNode("Teveligin")
    televegin.addChild(TreeNode("TV"))
    televegin.addChild(TreeNode("LG"))

    root.addChild(laptops)
    root.addChild(phonec)
    root.addChild(televegin)


    return root
# root = createTree()
# root.displayTree()