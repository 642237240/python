import wx
# import images


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "ToolBars", size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour("White")
        statusBar = self.CreateStatusBar()  # 1创建状态栏
        toolbar = self.CreateToolBar()  # 2创建工具栏
        # toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(), "New", "Long help for 'New'")  # 3给工具栏添加一个工具
        toolbar.Realize()  # 4准备显示工具栏
        menuBar = wx.MenuBar()  # 创建菜单栏
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "&Cut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
