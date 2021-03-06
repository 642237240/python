import wx
import sys


class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print("Frame __init__")
        wx.Frame.__init__(self, parent, id, title)


class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print("App __init__")
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print("OnInit")  # 输出到stdout
        self.frame = Frame(parent=None, id=-1, title='Startup')  # 创建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print("A pretend error message", file=sys.stderr)  # 输出到stderr
        return True

    def OnExit(self):
        print("OnExit")


if __name__ == "__main__":
    app = App(redirect=True, filename="output")  # 输出重定向到文件output
    print("before MainLoop")
    app.MainLoop()  # 2进入主事件循环
    print("after MainLoop")
