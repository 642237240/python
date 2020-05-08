'''
每个wxPython程序必须有一个应用程序（application）对象和至少一个框架（frame）对象。
application对象必须是wx.App的一个实例或在OnInit()方法中定义的一个子类的一个实例。
应用程序启动时，OnInit()方法将被wx.App父类调用。

'''
import wx   # 导入必须的wxPython包


class MyApp(wx.App):  # 子类化wxPython应用程序类
    def OnInit(self):   # 定义一个应用程序的初始化方法
        frame = wx.Frame(parent=None, id=-1, title='Bare')
        frame.Show()
        return True  # 此处返回False时，应用程序直接退出


app = MyApp()  # 创建一个应用程序类的实例
app.MainLoop()  # 进入这个应用程序的主事件循环
