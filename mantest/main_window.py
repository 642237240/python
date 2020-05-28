import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)

        self.panel = wx.Panel(self)

        menuBar = wx.MenuBar()
        menu_cfg = wx.Menu()
        menu_cfg.Append(-1, item='serial config', helpString='set serial config')
        menu_cfg.Append(-1, item='test config', helpString='set test config')
        menuBar.Append(menu_cfg, title='config')
        menu_help = wx.Menu()
        menu_help.Append(-1, item='about')
        menuBar.Append(menu_help, 'help')
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()

if __name__ =='__main__':
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()
