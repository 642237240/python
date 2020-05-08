'''Spare.py is a starting point for a wxPython program.'''  # 文档字符串保存在模块的__doc__属性中。可以print spare.__doc__
import wx


class Frame(wx.Frame):  # 定义一个Frame类作为wx.Frame的子类。
    pass


class App(wx.App):
    def OnInit(self):
        # 将frame实例的引用作为应用程序的一个实例
        self.frame = Frame(parent=None, title="Spare")
        self.frame.Show()
        # SetTopWindow()方法继承自wx.App父类，是一个可选方法，让wxPython知道哪个框架或对话框将被认为是主要的。一个wxPython可以有几个框架，其中有一个是被设计为应用程序的顶级窗口。
        self.SetTopWindow(self.frame)
        return True


# 是python中通常用来测试该模块是作为独立运行还是被另一个模块所导入，通过检查该模块的__name__属性来实现。
if __name__ == '__main__':
    app = App()
    app.MainLoop()
