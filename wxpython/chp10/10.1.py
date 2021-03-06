import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Simple Menu Example')
        p = wx.Panel(self)
        menuBar = wx.MenuBar()
        menu = wx.Menu("left")
        menuBar.Append(menu, "Left Menu")
        menu2 = wx.Menu()
        menuBar.Append(menu2, "Middle Menu")
        menu3 = wx.Menu()
        menuBar.Append(menu3, 'Right Menu')
        self.SetMenuBar(menuBar)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
