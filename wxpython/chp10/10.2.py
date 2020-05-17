import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Simple Menu Example')
        p = wx.Panel(self)
        self.CreateStatusBar()
        menu = wx.Menu("simple")
        simple = menu.Append(-1, 'Simple menu item', 'This is some help text')
        menu.AppendSeparator()
        exit = menu.Append(-1, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        menuBar = wx.MenuBar()
        menuBar.Append(menu, 'Simple Menu')
        self.SetMenuBar(menuBar)
    
    def OnSimple(self, event):
        wx.MessageBox('You selected the simple menu item')

    def OnExit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
