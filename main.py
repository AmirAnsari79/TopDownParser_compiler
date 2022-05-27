class TreeNode:
    def __init__(self, data: str):
        self.data = [char for char in data]
        self.flag = True
        self.S()

    def S(self):
        if self.data[0] == "a" and self.data[-1] == "b":
            self.data.pop(0)
            self.data.pop(-1)
            self.S1()
            if self.flag:
                self.S2()
        else:
            self.flag = False

    def S1(self):
        if self.data[0] == "a":
            self.data.pop(0)
            self.S1()
            self.S2()
            # if self.data[0] == "b":
            #     self.data.pop(0)
            # else:
            #     self.flag = False
        elif self.data[0] == "c":
            self.data.pop(0)
            # self.S2()
        else:
            self.flag = False

    def S2(self):
        if self.data[0] == "a":
            self.data.pop(0)
            self.S1()
            if len(self.data) > 0:
                self.S2()
        if len(self.data) > 0:
            if self.data[0] == "c":
                self.data.pop(0)
                if len(self.data) > 0:
                    if self.data[0] == "b":
                        self.data.pop(0)
                    else:
                        self.flag = False

    def result(self):
        print(self.flag)


if __name__ == "__main__":
    Root2 = TreeNode("acaccbb")
    Root3 = TreeNode("aaccbaccbb")
    Root = TreeNode("aacaccbbcb")
    Root1 = TreeNode("aaaccbaaccbcbbaaccbcbb")

    Root.result()
    Root1.result()
    Root2.result()
    Root3.result()
